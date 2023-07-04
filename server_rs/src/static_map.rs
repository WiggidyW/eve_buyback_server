pub const PRICE_VERSION: &str = "UNSET";

pub static MARKET_MAP: phf::Map<u64, &str> = phf::phf_map! {};

pub static REGION_MAP: phf::Map<&str, phf::Map<u32, (u8, u8, u8, u64)>> = phf::phf_map! {};
