import weve_esi_pb2 as _weve_esi_pb2
import buyback_pb2 as _buyback_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

BOTH: Query
CHARACTERS: AuthScope
CONTRACTS: AuthScope
DESCRIPTOR: _descriptor.FileDescriptor
FALSE: Query
ITEMS: AuthScope
READ: AuthKind
TRUE: Query
WRITE: AuthKind

class AddCharactersRep(_message.Message):
    __slots__ = ["authorized", "refresh_token"]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorized: bool
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ..., authorized: bool = ...) -> None: ...

class AddCharactersReq(_message.Message):
    __slots__ = ["auth_kind", "auth_scope", "characters", "name", "refresh_token"]
    AUTH_KIND_FIELD_NUMBER: _ClassVar[int]
    AUTH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    auth_kind: AuthKind
    auth_scope: AuthScope
    characters: _containers.RepeatedScalarFieldContainer[str]
    name: str
    refresh_token: str
    def __init__(self, name: _Optional[str] = ..., auth_kind: _Optional[_Union[AuthKind, str]] = ..., auth_scope: _Optional[_Union[AuthScope, str]] = ..., refresh_token: _Optional[str] = ..., characters: _Optional[_Iterable[str]] = ...) -> None: ...

class BuybackContract(_message.Message):
    __slots__ = ["buy_contract", "check_contract", "esi_contract", "hash_code"]
    BUY_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CHECK_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ESI_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    HASH_CODE_FIELD_NUMBER: _ClassVar[int]
    buy_contract: _buyback_pb2.Rep
    check_contract: _buyback_pb2.Rep
    esi_contract: _weve_esi_pb2.ExchangeContract
    hash_code: str
    def __init__(self, esi_contract: _Optional[_Union[_weve_esi_pb2.ExchangeContract, _Mapping]] = ..., check_contract: _Optional[_Union[_buyback_pb2.Rep, _Mapping]] = ..., buy_contract: _Optional[_Union[_buyback_pb2.Rep, _Mapping]] = ..., hash_code: _Optional[str] = ...) -> None: ...

class BuybackContractsRep(_message.Message):
    __slots__ = ["authorized", "contracts", "refresh_token"]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorized: bool
    contracts: _containers.RepeatedCompositeFieldContainer[BuybackContract]
    refresh_token: str
    def __init__(self, contracts: _Optional[_Iterable[_Union[BuybackContract, _Mapping]]] = ..., refresh_token: _Optional[str] = ..., authorized: bool = ...) -> None: ...

class BuybackContractsReq(_message.Message):
    __slots__ = ["include_buy", "include_check", "include_items", "language", "refresh_token"]
    INCLUDE_BUY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CHECK_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    include_buy: bool
    include_check: bool
    include_items: bool
    language: str
    refresh_token: str
    def __init__(self, include_items: bool = ..., include_check: bool = ..., include_buy: bool = ..., refresh_token: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class DelCharactersRep(_message.Message):
    __slots__ = ["authorized", "refresh_token"]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorized: bool
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ..., authorized: bool = ...) -> None: ...

class DelCharactersReq(_message.Message):
    __slots__ = ["auth_kind", "auth_scope", "characters", "name", "refresh_token"]
    AUTH_KIND_FIELD_NUMBER: _ClassVar[int]
    AUTH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    auth_kind: AuthKind
    auth_scope: AuthScope
    characters: _containers.RepeatedScalarFieldContainer[str]
    name: str
    refresh_token: str
    def __init__(self, name: _Optional[str] = ..., auth_kind: _Optional[_Union[AuthKind, str]] = ..., auth_scope: _Optional[_Union[AuthScope, str]] = ..., refresh_token: _Optional[str] = ..., characters: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCharactersRep(_message.Message):
    __slots__ = ["authorized", "characters", "refresh_token"]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorized: bool
    characters: _containers.RepeatedScalarFieldContainer[str]
    refresh_token: str
    def __init__(self, characters: _Optional[_Iterable[str]] = ..., refresh_token: _Optional[str] = ..., authorized: bool = ...) -> None: ...

class ListCharactersReq(_message.Message):
    __slots__ = ["auth_kind", "auth_scope", "name", "refresh_token"]
    AUTH_KIND_FIELD_NUMBER: _ClassVar[int]
    AUTH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    auth_kind: AuthKind
    auth_scope: AuthScope
    name: str
    refresh_token: str
    def __init__(self, name: _Optional[str] = ..., auth_kind: _Optional[_Union[AuthKind, str]] = ..., auth_scope: _Optional[_Union[AuthScope, str]] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class ListItem(_message.Message):
    __slots__ = ["category_idx", "enabled", "group_idx", "json_idx", "market_group_idx", "name", "type_id"]
    class JsonIdxEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    CATEGORY_IDX_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDX_FIELD_NUMBER: _ClassVar[int]
    JSON_IDX_FIELD_NUMBER: _ClassVar[int]
    MARKET_GROUP_IDX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    category_idx: int
    enabled: bool
    group_idx: int
    json_idx: _containers.ScalarMap[str, int]
    market_group_idx: int
    name: str
    type_id: int
    def __init__(self, type_id: _Optional[int] = ..., enabled: bool = ..., json_idx: _Optional[_Mapping[str, int]] = ..., name: _Optional[str] = ..., market_group_idx: _Optional[int] = ..., group_idx: _Optional[int] = ..., category_idx: _Optional[int] = ...) -> None: ...

class ListRep(_message.Message):
    __slots__ = ["authorized", "categories", "groups", "items", "json", "market_groups", "refresh_token"]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    MARKET_GROUPS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorized: bool
    categories: _containers.RepeatedScalarFieldContainer[str]
    groups: _containers.RepeatedScalarFieldContainer[str]
    items: _containers.RepeatedCompositeFieldContainer[ListItem]
    json: _containers.RepeatedScalarFieldContainer[str]
    market_groups: _containers.RepeatedScalarFieldContainer[str]
    refresh_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[ListItem, _Mapping]]] = ..., json: _Optional[_Iterable[str]] = ..., market_groups: _Optional[_Iterable[str]] = ..., groups: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., refresh_token: _Optional[str] = ..., authorized: bool = ...) -> None: ...

class ListReq(_message.Message):
    __slots__ = ["include_category", "include_configured", "include_enabled", "include_group", "include_json", "include_market_group", "include_name", "language", "name", "refresh_token"]
    INCLUDE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_GROUP_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_JSON_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MARKET_GROUP_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    include_category: bool
    include_configured: Query
    include_enabled: Query
    include_group: bool
    include_json: bool
    include_market_group: bool
    include_name: bool
    language: str
    name: str
    refresh_token: str
    def __init__(self, name: _Optional[str] = ..., refresh_token: _Optional[str] = ..., include_enabled: _Optional[_Union[Query, str]] = ..., include_configured: _Optional[_Union[Query, str]] = ..., include_json: bool = ..., language: _Optional[str] = ..., include_name: bool = ..., include_market_group: bool = ..., include_group: bool = ..., include_category: bool = ...) -> None: ...

class UpdateItem(_message.Message):
    __slots__ = ["enabled", "json_idx", "type_id"]
    class JsonIdxEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    JSON_IDX_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    json_idx: _containers.ScalarMap[str, int]
    type_id: int
    def __init__(self, type_id: _Optional[int] = ..., enabled: bool = ..., json_idx: _Optional[_Mapping[str, int]] = ...) -> None: ...

class UpdateRep(_message.Message):
    __slots__ = ["authorized", "refresh_token"]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorized: bool
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ..., authorized: bool = ...) -> None: ...

class UpdateReq(_message.Message):
    __slots__ = ["items", "json", "name", "refresh_token"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[UpdateItem]
    json: _containers.RepeatedScalarFieldContainer[str]
    name: str
    refresh_token: str
    def __init__(self, name: _Optional[str] = ..., refresh_token: _Optional[str] = ..., items: _Optional[_Iterable[_Union[UpdateItem, _Mapping]]] = ..., json: _Optional[_Iterable[str]] = ...) -> None: ...

class Query(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AuthKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AuthScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
