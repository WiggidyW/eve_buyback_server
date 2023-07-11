pub mod weve_esi_proto;
pub use weve_esi_proto as weve_esi;
pub use weve_esi_proto::{WeveEsi, WeveEsiClient};

pub mod buyback_proto;
pub use buyback_proto as buyback;
pub use buyback_proto::buyback_server;

use std::hash::{Hash, Hasher};
impl Hash for weve_esi::MarketOrdersReq {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.location_id.hash(state);
        self.type_id.hash(state);
        self.token.hash(state);
        self.buy.hash(state);
    }
}

impl Eq for weve_esi::MarketOrdersReq {}
