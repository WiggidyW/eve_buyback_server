use super::{
    super::{PriceModelStore, TokenStore},
    item_model::ItemModel,
    price_model::{FulfilledPriceModelRequests, PriceModel, PriceModelRequest, PriceModelRequests},
    PriceModelResponse,
};
use crate::{error::Error, pb, typedb::TypeDb};

#[derive(Debug)]
pub struct ReprocessModel {
    pub efficiency: f64,
}

impl ReprocessModel {
    pub async fn to_requests(
        &self,
        req_item: pb::buyback::ReqItem,
        type_db: &impl TypeDb,
        token_store: &impl TokenStore,
        model_store: &impl PriceModelStore,
        region: &str,
    ) -> Result<PriceModelRequests, Error> {
        let children = type_db.get_reprocess(req_item.type_id).await?;
        let mut reqs = Vec::with_capacity(children.len() + 1);
        let quantity = req_item.quantity as f64;

        reqs.push(PriceModelRequest {
            type_id: req_item.type_id,
            parent_type_id: req_item.type_id,
            quantity: quantity,
            item_req: None,
        });

        for (child_type_id, child_quantity) in children {
            reqs.push(PriceModelRequest {
                type_id: child_type_id,
                parent_type_id: req_item.type_id,
                quantity: child_quantity * quantity * self.efficiency,
                item_req: match model_store.get_price_model(region, &child_type_id) {
                    PriceModel::Item(item_model) => Some(
                        item_model
                            .to_request(child_type_id, token_store.get_token(&item_model.location)),
                    ),
                    _ => None,
                },
            })
        }

        Ok(PriceModelRequests::Multi(reqs))
    }

    pub async fn to_requests_as(
        &self,
        req_item: pb::buyback::ReqItem,
        type_db: &impl TypeDb,
        token_store: &impl TokenStore,
        item_model: &ItemModel,
    ) -> Result<PriceModelRequests, Error> {
        let children = type_db.get_reprocess(req_item.type_id).await?;
        let mut reqs = Vec::with_capacity(children.len() + 1);
        let quantity = req_item.quantity as f64;
        let refresh_token = token_store.get_token(&item_model.location);

        reqs.push(PriceModelRequest {
            type_id: req_item.type_id,
            parent_type_id: req_item.type_id,
            quantity: quantity,
            item_req: None,
        });

        for (child_type_id, child_quantity) in children {
            reqs.push(PriceModelRequest {
                type_id: child_type_id,
                parent_type_id: req_item.type_id,
                quantity: child_quantity * quantity * self.efficiency,
                item_req: Some(item_model.to_request(child_type_id, refresh_token.clone())),
            });
        }

        Ok(PriceModelRequests::Multi(reqs))
    }

    pub fn into_rep_items(self, reqs: FulfilledPriceModelRequests) -> PriceModelResponse {
        let mut sum = 0.0;
        let fulfilled_reqs = reqs.multi_unchecked();
        let mut rep_items = Vec::with_capacity(fulfilled_reqs.len());
        let mut parent_item = None;

        for req in fulfilled_reqs {
            if req.type_id == req.parent_type_id {
                parent_item = Some(req);
                continue;
            } else {
                match req.item_req {
                    Some(item_req) => {
                        let rep_item = item_req.item_model.clone().into_rep_item(
                            req.type_id,
                            req.parent_type_id,
                            req.quantity,
                            req.item_name,
                            req.market_name,
                            item_req,
                        );
                        sum += rep_item.price_per * rep_item.quantity;
                        rep_items.push(rep_item);
                    }
                    None => rep_items.push(pb::buyback::RepItem {
                        type_id: req.type_id,
                        parent_type_id: req.parent_type_id,
                        quantity: req.quantity,
                        name: req.item_name,
                        price_per: 0.0,
                        description: "Rejected".to_string(),
                        accepted: false,
                        meta: None,
                    }),
                };
            }
        }

        let parent_item = parent_item.unwrap();
        let price_per = sum / parent_item.quantity;
        let (description, accepted) = match price_per > 0.0 {
            true => (format!("{}% Reprocessed", self.efficiency * 100.0), true),
            false => (
                format!(
                    "{}% Reprocessed - All reprocessed items rejected",
                    self.efficiency * 100.0
                ),
                false,
            ),
        };

        rep_items.push(pb::buyback::RepItem {
            type_id: parent_item.type_id,
            parent_type_id: parent_item.parent_type_id,
            quantity: parent_item.quantity,
            name: parent_item.item_name,
            price_per: price_per,
            description: description,
            accepted: accepted,
            meta: None,
        });
        let parent_item_idx = rep_items.len() - 1;
        rep_items.swap(0, parent_item_idx);

        PriceModelResponse::Multi(rep_items)
    }
}
