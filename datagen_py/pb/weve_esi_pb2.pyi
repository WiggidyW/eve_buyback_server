from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActiveOrder(_message.Message):
    __slots__ = ["buy", "price", "quantity"]
    BUY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    buy: bool
    price: float
    quantity: int
    def __init__(self, buy: bool = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ...) -> None: ...

class ActiveOrdersRep(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LocationActiveOrders
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LocationActiveOrders, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[int, LocationActiveOrders]
    def __init__(self, inner: _Optional[_Mapping[int, LocationActiveOrders]] = ...) -> None: ...

class ActiveOrdersReq(_message.Message):
    __slots__ = ["characters", "corporations"]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    CORPORATIONS_FIELD_NUMBER: _ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[Entity]
    corporations: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, characters: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., corporations: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

class AdjustedPriceRep(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.ScalarMap[int, float]
    def __init__(self, inner: _Optional[_Mapping[int, float]] = ...) -> None: ...

class AdjustedPriceReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Asset(_message.Message):
    __slots__ = ["entity_id", "flags", "material_efficiency", "quantity", "runs", "time_efficiency"]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    TIME_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    flags: _containers.RepeatedScalarFieldContainer[str]
    material_efficiency: int
    quantity: int
    runs: int
    time_efficiency: int
    def __init__(self, entity_id: _Optional[int] = ..., quantity: _Optional[int] = ..., runs: _Optional[int] = ..., material_efficiency: _Optional[int] = ..., time_efficiency: _Optional[int] = ..., flags: _Optional[_Iterable[str]] = ...) -> None: ...

class AssetsRep(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LocationAssets
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LocationAssets, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[int, LocationAssets]
    def __init__(self, inner: _Optional[_Mapping[int, LocationAssets]] = ...) -> None: ...

class AssetsReq(_message.Message):
    __slots__ = ["characters", "corporations"]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    CORPORATIONS_FIELD_NUMBER: _ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[Entity]
    corporations: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, characters: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., corporations: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ["id", "token"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: int
    token: str
    def __init__(self, id: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class ExchangeContract(_message.Message):
    __slots__ = ["char_id", "corp_id", "description", "expires", "is_corp", "issued", "items", "location_id", "price", "region_id", "reward", "system_id", "volume"]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    CORP_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    ISSUED_FIELD_NUMBER: _ClassVar[int]
    IS_CORP_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    corp_id: int
    description: str
    expires: int
    is_corp: bool
    issued: int
    items: _containers.RepeatedCompositeFieldContainer[ExchangeContractItem]
    location_id: int
    price: float
    region_id: int
    reward: float
    system_id: int
    volume: float
    def __init__(self, items: _Optional[_Iterable[_Union[ExchangeContractItem, _Mapping]]] = ..., location_id: _Optional[int] = ..., description: _Optional[str] = ..., price: _Optional[float] = ..., reward: _Optional[float] = ..., expires: _Optional[int] = ..., issued: _Optional[int] = ..., volume: _Optional[float] = ..., char_id: _Optional[int] = ..., corp_id: _Optional[int] = ..., is_corp: bool = ..., system_id: _Optional[int] = ..., region_id: _Optional[int] = ...) -> None: ...

class ExchangeContractItem(_message.Message):
    __slots__ = ["quantity", "type_id"]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    type_id: int
    def __init__(self, type_id: _Optional[int] = ..., quantity: _Optional[int] = ...) -> None: ...

class ExchangeContractsRep(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.RepeatedCompositeFieldContainer[ExchangeContract]
    def __init__(self, inner: _Optional[_Iterable[_Union[ExchangeContract, _Mapping]]] = ...) -> None: ...

class ExchangeContractsReq(_message.Message):
    __slots__ = ["active_only", "characters", "corporations", "include_items"]
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    CORPORATIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    active_only: bool
    characters: _containers.RepeatedCompositeFieldContainer[Entity]
    corporations: _containers.RepeatedCompositeFieldContainer[Entity]
    include_items: bool
    def __init__(self, characters: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., corporations: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., active_only: bool = ..., include_items: bool = ...) -> None: ...

class IndustryJob(_message.Message):
    __slots__ = ["activity", "blueprint_id", "character_id", "finish", "is_bpc", "location_id", "material_efficiency", "probability", "product_id", "runs", "start", "time_efficiency"]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    BLUEPRINT_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    FINISH_FIELD_NUMBER: _ClassVar[int]
    IS_BPC_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    TIME_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    activity: int
    blueprint_id: int
    character_id: int
    finish: int
    is_bpc: bool
    location_id: int
    material_efficiency: int
    probability: float
    product_id: int
    runs: int
    start: int
    time_efficiency: int
    def __init__(self, location_id: _Optional[int] = ..., character_id: _Optional[int] = ..., start: _Optional[int] = ..., finish: _Optional[int] = ..., probability: _Optional[float] = ..., product_id: _Optional[int] = ..., blueprint_id: _Optional[int] = ..., material_efficiency: _Optional[int] = ..., time_efficiency: _Optional[int] = ..., activity: _Optional[int] = ..., runs: _Optional[int] = ..., is_bpc: bool = ...) -> None: ...

class IndustryJobsRep(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.RepeatedCompositeFieldContainer[IndustryJob]
    def __init__(self, inner: _Optional[_Iterable[_Union[IndustryJob, _Mapping]]] = ...) -> None: ...

class IndustryJobsReq(_message.Message):
    __slots__ = ["characters", "corporations"]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    CORPORATIONS_FIELD_NUMBER: _ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[Entity]
    corporations: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, characters: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., corporations: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

class LocationActiveOrders(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TypeActiveOrders
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TypeActiveOrders, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[int, TypeActiveOrders]
    def __init__(self, inner: _Optional[_Mapping[int, TypeActiveOrders]] = ...) -> None: ...

class LocationAssets(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TypeAssets
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TypeAssets, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[int, TypeAssets]
    def __init__(self, inner: _Optional[_Mapping[int, TypeAssets]] = ...) -> None: ...

class LocationTransactions(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TypeTransactions
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TypeTransactions, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[int, TypeTransactions]
    def __init__(self, inner: _Optional[_Mapping[int, TypeTransactions]] = ...) -> None: ...

class MarketOrder(_message.Message):
    __slots__ = ["price", "quantity"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    price: float
    quantity: int
    def __init__(self, quantity: _Optional[int] = ..., price: _Optional[float] = ...) -> None: ...

class MarketOrdersRep(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.RepeatedCompositeFieldContainer[MarketOrder]
    def __init__(self, inner: _Optional[_Iterable[_Union[MarketOrder, _Mapping]]] = ...) -> None: ...

class MarketOrdersReq(_message.Message):
    __slots__ = ["buy", "location_id", "token", "type_id"]
    BUY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    buy: bool
    location_id: int
    token: str
    type_id: int
    def __init__(self, location_id: _Optional[int] = ..., type_id: _Optional[int] = ..., token: _Optional[str] = ..., buy: bool = ...) -> None: ...

class MultiMarketOrderRep(_message.Message):
    __slots__ = ["rep", "req"]
    REP_FIELD_NUMBER: _ClassVar[int]
    REQ_FIELD_NUMBER: _ClassVar[int]
    rep: MarketOrdersRep
    req: MarketOrdersReq
    def __init__(self, req: _Optional[_Union[MarketOrdersReq, _Mapping]] = ..., rep: _Optional[_Union[MarketOrdersRep, _Mapping]] = ...) -> None: ...

class MultiMarketOrdersRep(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.RepeatedCompositeFieldContainer[MultiMarketOrderRep]
    def __init__(self, inner: _Optional[_Iterable[_Union[MultiMarketOrderRep, _Mapping]]] = ...) -> None: ...

class MultiMarketOrdersReq(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.RepeatedCompositeFieldContainer[MarketOrdersReq]
    def __init__(self, inner: _Optional[_Iterable[_Union[MarketOrdersReq, _Mapping]]] = ...) -> None: ...

class Skills(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.ScalarMap[int, int]
    def __init__(self, inner: _Optional[_Mapping[int, int]] = ...) -> None: ...

class SkillsRep(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Skills
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Skills, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[int, Skills]
    def __init__(self, inner: _Optional[_Mapping[int, Skills]] = ...) -> None: ...

class SkillsReq(_message.Message):
    __slots__ = ["characters"]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[Entity]
    def __init__(self, characters: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ...) -> None: ...

class SystemIndex(_message.Message):
    __slots__ = ["copying", "invention", "manufacturing", "reactions", "research_me", "research_te"]
    COPYING_FIELD_NUMBER: _ClassVar[int]
    INVENTION_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURING_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_ME_FIELD_NUMBER: _ClassVar[int]
    RESEARCH_TE_FIELD_NUMBER: _ClassVar[int]
    copying: float
    invention: float
    manufacturing: float
    reactions: float
    research_me: float
    research_te: float
    def __init__(self, manufacturing: _Optional[float] = ..., research_te: _Optional[float] = ..., research_me: _Optional[float] = ..., copying: _Optional[float] = ..., invention: _Optional[float] = ..., reactions: _Optional[float] = ...) -> None: ...

class SystemIndexRep(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SystemIndex
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SystemIndex, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[int, SystemIndex]
    def __init__(self, inner: _Optional[_Mapping[int, SystemIndex]] = ...) -> None: ...

class SystemIndexReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Transaction(_message.Message):
    __slots__ = ["buy", "price", "quantity"]
    BUY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    buy: bool
    price: float
    quantity: int
    def __init__(self, buy: bool = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ...) -> None: ...

class TransactionsRep(_message.Message):
    __slots__ = ["inner"]
    class InnerEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LocationTransactions
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LocationTransactions, _Mapping]] = ...) -> None: ...
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.MessageMap[int, LocationTransactions]
    def __init__(self, inner: _Optional[_Mapping[int, LocationTransactions]] = ...) -> None: ...

class TransactionsReq(_message.Message):
    __slots__ = ["characters", "corporations", "since"]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    CORPORATIONS_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[Entity]
    corporations: _containers.RepeatedCompositeFieldContainer[Entity]
    since: int
    def __init__(self, characters: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., corporations: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., since: _Optional[int] = ...) -> None: ...

class TypeActiveOrders(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.RepeatedCompositeFieldContainer[ActiveOrder]
    def __init__(self, inner: _Optional[_Iterable[_Union[ActiveOrder, _Mapping]]] = ...) -> None: ...

class TypeAssets(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.RepeatedCompositeFieldContainer[Asset]
    def __init__(self, inner: _Optional[_Iterable[_Union[Asset, _Mapping]]] = ...) -> None: ...

class TypeTransactions(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, inner: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...
