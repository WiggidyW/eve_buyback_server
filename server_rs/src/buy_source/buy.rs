use super::{
    price_model::{
        FulfilledItemModelRequest, FulfilledPriceModelRequest, FulfilledPriceModelRequests,
        PriceModelRequest, PriceModelRequests, PriceModelResponse,
    },
    MarketNameStore, PriceModelStore, TokenStore,
};
use crate::{
    error::Error,
    pb::{self, WeveEsi},
    typedb::TypeDb,
};
use futures::{stream::FuturesUnordered, Future, StreamExt};
use std::{
    collections::{hash_map::DefaultHasher, HashMap, HashSet},
    hash::{Hash, Hasher},
};

async fn get_fulfilled_request<F>(
    mreq: PriceModelRequest,
    item_names: &mut HashMap<u32, String>,
    item_name_futs: &mut HashMap<u32, F>,
    market_store: &impl MarketNameStore,
    esi_rep: &HashMap<pb::weve_esi::MarketOrdersReq, pb::weve_esi::MarketOrdersRep>,
) -> Result<FulfilledPriceModelRequest, Error>
where
    F: Future<Output = Result<String, Error>> + Send,
{
    Ok(FulfilledPriceModelRequest {
        type_id: mreq.type_id,
        parent_type_id: mreq.parent_type_id,
        quantity: mreq.quantity,
        item_name: match item_names.get(&mreq.type_id) {
            Some(name) => name.clone(),
            None => {
                let name = item_name_futs
                    .remove(&mreq.type_id)
                    .expect("Missing item name future")
                    .await?;
                item_names.insert(mreq.type_id, name.clone());
                name
            }
        },
        market_name: match mreq.item_req {
            Some(ref item_req) => market_store.get_market_name(&item_req.item_model.location),
            None => "".to_string(),
        },
        item_req: match mreq.item_req {
            Some(item_req) => match esi_rep.get(&item_req.req) {
                Some(rep) => Some(FulfilledItemModelRequest {
                    item_model: item_req.item_model,
                    req: item_req.req,
                    rep: rep.clone(),
                }),
                None => None,
            },
            None => None,
        },
    })
}

pub async fn buy(
    req: pb::buyback::BuyReq,
    typedb: &impl TypeDb,
    market_store: &impl MarketNameStore,
    token_store: &impl TokenStore,
    model_store: &impl PriceModelStore,
    client: &pb::WeveEsiClient,
) -> Result<pb::buyback::Rep, Error> {
    let timestamp = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .expect("Time went backwards")
        .as_secs();

    let item_len = req.items.len();
    let mut item_name_futs = HashMap::with_capacity(req.items.len());
    let mut model_req_futs = FuturesUnordered::new();

    for item in req.items {
        if !item_name_futs.contains_key(&item.type_id) {
            let item_name_fut = typedb.get_name(item.type_id, &req.language);
            item_name_futs.insert(item.type_id, item_name_fut);
        }

        let model = model_store.get_price_model(&req.location, &item.type_id);
        let model_req_fut =
            model.into_requests(item, typedb, token_store, model_store, &req.location);
        model_req_futs.push(model_req_fut);
    }

    let mut num_reqs = 0;
    let mut models_with_reqs = Vec::with_capacity(item_len);
    let mut esi_reqs = HashSet::with_capacity(item_len);

    while let Some(model_req) = model_req_futs.next().await {
        let (model_reqs, model) = model_req?;
        num_reqs += model_reqs.len();
        match model_reqs {
            PriceModelRequests::Single(ref mreq) => {
                if !item_name_futs.contains_key(&mreq.type_id) {
                    let item_name_fut = typedb.get_name(mreq.type_id, &req.language);
                    item_name_futs.insert(mreq.type_id, item_name_fut);
                }
                if let Some(ref ireq) = mreq.item_req {
                    esi_reqs.insert(ireq.req.clone());
                }
            }
            PriceModelRequests::Multi(ref mreqs) => {
                for mreq in mreqs {
                    if !item_name_futs.contains_key(&mreq.type_id) {
                        let item_name_fut = typedb.get_name(mreq.type_id, &req.language);
                        item_name_futs.insert(mreq.type_id, item_name_fut);
                    }
                    if let Some(ref ireq) = mreq.item_req {
                        esi_reqs.insert(ireq.req.clone());
                    }
                }
            }
        }
        models_with_reqs.push((model, model_reqs));
    }

    drop(model_req_futs);

    let esi_rep = client
        .clone()
        .multi_market_orders(
            pb::weve_esi::MultiMarketOrdersReq {
                inner: esi_reqs.into_iter().collect(),
            }
            .into(),
        )
        .await
        .map_err(|e| Error::WeveEsi(e))?
        .output
        .inner
        .into_iter()
        .filter_map(|r| match (r.req, r.rep) {
            (Some(req), Some(rep)) => Some((req, rep)),
            _ => None,
        })
        .collect::<HashMap<_, _>>();

    let mut item_names: HashMap<u32, String> = HashMap::with_capacity(item_name_futs.len());
    let version = model_store.get_version();
    let mut sum = 0.0;

    let mut hasher = DefaultHasher::new();
    req.location.hash(&mut hasher);
    version.hash(&mut hasher);

    let mut rep_items = Vec::with_capacity(num_reqs);
    for (model, model_req) in models_with_reqs {
        let fulfilled_req = match model_req {
            PriceModelRequests::Single(mreq) => FulfilledPriceModelRequests::Single(
                get_fulfilled_request(
                    mreq,
                    &mut item_names,
                    &mut item_name_futs,
                    market_store,
                    &esi_rep,
                )
                .await?,
            ),
            PriceModelRequests::Multi(mreqs) => {
                let mut fulfilled_mreqs = Vec::with_capacity(mreqs.len());
                for mreq in mreqs {
                    fulfilled_mreqs.push(
                        get_fulfilled_request(
                            mreq,
                            &mut item_names,
                            &mut item_name_futs,
                            market_store,
                            &esi_rep,
                        )
                        .await?,
                    );
                }
                FulfilledPriceModelRequests::Multi(fulfilled_mreqs)
            }
        };
        match model.into_rep_items(fulfilled_req) {
            PriceModelResponse::Single(item) => {
                item.type_id.hash(&mut hasher);
                sum += item.price_per * item.quantity;
                rep_items.push(item);
            }
            PriceModelResponse::Multi(items) => {
                sum += items[0].price_per * items[0].quantity;
                for item in items {
                    item.type_id.hash(&mut hasher);
                    rep_items.push(item);
                }
            }
        };
    }

    Ok(pb::buyback::Rep {
        items: rep_items,
        hash: {
            if sum > 0.0 {
                (sum as u64).hash(&mut hasher);
                format!("{:x}", hasher.finish())
            } else {
                "".to_string()
            }
        },
        sum: sum,
        timestamp: timestamp,
        version: version.to_string(),
        location: req.location,
    })
}
