use super::{
    super::{PriceModelStore, TokenStore},
    item_model::{FulfilledItemModelRequest, ItemModel, ItemModelRequest},
    reprocess_model::ReprocessModel,
};
use crate::{error::Error, pb, typedb::TypeDb};

#[derive(Debug)]
pub enum PriceModelResponse {
    Single(pb::buyback::RepItem),
    Multi(Vec<pb::buyback::RepItem>),
}

#[derive(Debug)]
pub struct PriceModelRequest {
    pub type_id: u32,
    pub parent_type_id: u32,
    pub quantity: f64,
    pub item_req: Option<ItemModelRequest>,
}

#[derive(Debug)]
pub enum PriceModelRequests {
    Single(PriceModelRequest),
    Multi(Vec<PriceModelRequest>),
}

impl PriceModelRequests {
    pub fn len(&self) -> usize {
        match self {
            PriceModelRequests::Single(_) => 1,
            PriceModelRequests::Multi(r) => r.len(),
        }
    }
}

#[derive(Debug)]
pub struct FulfilledPriceModelRequest {
    pub type_id: u32,
    pub parent_type_id: u32,
    pub quantity: f64,
    pub item_name: String,
    pub market_name: String,
    pub item_req: Option<FulfilledItemModelRequest>,
}

#[derive(Debug)]
pub enum FulfilledPriceModelRequests {
    Single(FulfilledPriceModelRequest),
    Multi(Vec<FulfilledPriceModelRequest>),
}

impl FulfilledPriceModelRequests {
    pub fn single_unchecked(self) -> FulfilledPriceModelRequest {
        match self {
            FulfilledPriceModelRequests::Single(r) => r,
            FulfilledPriceModelRequests::Multi(_) => {
                panic!("Expected single request")
            }
        }
    }

    pub fn multi_unchecked(self) -> Vec<FulfilledPriceModelRequest> {
        match self {
            FulfilledPriceModelRequests::Multi(r) => r,
            FulfilledPriceModelRequests::Single(_) => {
                panic!("Expected multi request")
            }
        }
    }
}

#[derive(Debug)]
pub enum PriceModel {
    Rejected,
    Item(ItemModel),
    Reprocess(ReprocessModel),
    ReprocessAs(ItemModel, ReprocessModel),
}

impl PriceModel {
    pub async fn into_requests(
        self,
        req_item: pb::buyback::ReqItem,
        type_db: &impl TypeDb,
        token_store: &impl TokenStore,
        model_store: &impl PriceModelStore,
        region: &str,
    ) -> Result<(PriceModelRequests, Self), Error> {
        Ok((
            match self {
                PriceModel::Rejected => PriceModelRequests::Single(PriceModelRequest {
                    type_id: req_item.type_id,
                    parent_type_id: req_item.type_id,
                    quantity: req_item.quantity as f64,
                    item_req: None,
                }),
                PriceModel::Item(ref i) => PriceModelRequests::Single(PriceModelRequest {
                    type_id: req_item.type_id,
                    parent_type_id: req_item.type_id,
                    quantity: req_item.quantity as f64,
                    item_req: Some(
                        i.to_request(req_item.type_id, token_store.get_token(&i.location)),
                    ),
                }),
                PriceModel::Reprocess(ref r) => {
                    r.to_requests(req_item, type_db, token_store, model_store, region)
                        .await?
                }
                PriceModel::ReprocessAs(ref i, ref r) => {
                    r.to_requests_as(req_item, type_db, token_store, i).await?
                }
            },
            self,
        ))
    }

    pub fn into_rep_items(self, reqs: FulfilledPriceModelRequests) -> PriceModelResponse {
        match self {
            PriceModel::Rejected => {
                let fulfilled_req = reqs.single_unchecked();
                PriceModelResponse::Single(pb::buyback::RepItem {
                    type_id: fulfilled_req.type_id,
                    parent_type_id: fulfilled_req.parent_type_id,
                    quantity: fulfilled_req.quantity,
                    name: fulfilled_req.item_name,
                    price_per: 0.0,
                    description: "Rejected".to_string(),
                    accepted: false,
                    meta: None,
                })
            }
            PriceModel::Item(i) => {
                let fulfilled_req = reqs.single_unchecked();
                PriceModelResponse::Single(i.into_rep_item(
                    fulfilled_req.type_id,
                    fulfilled_req.parent_type_id,
                    fulfilled_req.quantity,
                    fulfilled_req.item_name,
                    fulfilled_req.market_name,
                    fulfilled_req.item_req.unwrap(),
                ))
            }
            PriceModel::Reprocess(r) => r.into_rep_items(reqs),
            PriceModel::ReprocessAs(_, r) => r.into_rep_items(reqs),
        }
    }
}
