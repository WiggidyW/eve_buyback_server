use super::order_target::OrderTarget;
use crate::pb;

pub fn get_price_from_orders(
    orders: Vec<pb::weve_esi::MarketOrder>,
    order_target: OrderTarget,
) -> Option<f64> {
    match (orders.len(), order_target) {
        (0, _) => None,
        (_, OrderTarget::MaxBuy) => {
            let mut highest = orders[0].price;
            for order in orders {
                if order.price > highest {
                    highest = order.price;
                }
            }
            Some(highest)
        }
        (_, OrderTarget::MinSell) => {
            let mut lowest = orders[0].price;
            for order in orders {
                if order.price < lowest {
                    lowest = order.price;
                }
            }
            Some(lowest)
        }
    }
}
