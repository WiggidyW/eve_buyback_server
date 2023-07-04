use crate::static_map::MARKET_MAP;

pub trait MarketNameStore: Send + Sync + 'static {
    fn get_market_name(&self, location: &u64) -> String;
}

#[derive(Debug)]
pub struct MarketNameStoreMarker;

impl MarketNameStore for MarketNameStoreMarker {
    fn get_market_name(&self, location: &u64) -> String {
        MARKET_MAP
            .get(location)
            .expect(&format!("Market name missing for location: {}", location))
            .to_string()
    }
}

pub fn new_market_name_store() -> impl MarketNameStore {
    return MarketNameStoreMarker;
}
