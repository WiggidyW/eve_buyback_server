use super::{get_price::get_price_from_orders, order_target::OrderTarget};
use crate::pb;

#[derive(Debug)]
pub struct ItemModelRequest {
    pub item_model: ItemModel,
    pub req: pb::weve_esi::MarketOrdersReq,
}

#[derive(Debug)]
pub struct FulfilledItemModelRequest {
    pub item_model: ItemModel,
    pub req: pb::weve_esi::MarketOrdersReq,
    pub rep: pb::weve_esi::MarketOrdersRep,
}

#[derive(Debug, Clone)]
pub struct ItemModel {
    pub order_target: OrderTarget,
    pub modifier: f64,
    pub location: u64,
}

impl ItemModel {
    pub fn to_request(&self, type_id: u32, refresh_token: String) -> ItemModelRequest {
        ItemModelRequest {
            req: pb::weve_esi::MarketOrdersReq {
                location_id: self.location,
                type_id: type_id,
                token: refresh_token,
                buy: self.order_target.is_buy(),
            },
            item_model: self.clone(),
        }
    }

    pub fn into_rep_item(
        self,
        type_id: u32,
        parent_type_id: u32,
        quantity: f64,
        item_name: String,
        market_name: String,
        req: FulfilledItemModelRequest,
    ) -> pb::buyback::RepItem {
        let (accepted, price_per, description) =
            match get_price_from_orders(req.rep.inner, self.order_target) {
                Some(price_per) => (
                    true,
                    price_per * self.modifier,
                    format!(
                        "{} {}% {}",
                        market_name,
                        self.modifier * 100.0,
                        self.order_target.to_string(),
                    ),
                ),
                None => (
                    false,
                    0.0,
                    format!(
                        "{} {}% {} - No orders found at {}",
                        market_name,
                        self.modifier * 100.0,
                        self.order_target.to_string(),
                        market_name,
                    ),
                ),
            };

        pb::buyback::RepItem {
            type_id: type_id,
            parent_type_id: parent_type_id,
            quantity: quantity,
            name: item_name,
            price_per: price_per,
            description: description,
            accepted: accepted,
            meta: None,
        }
    }
}
