from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuyReq(_message.Message):
    __slots__ = ["items", "language", "location"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReqItem]
    language: str
    location: str
    def __init__(self, items: _Optional[_Iterable[_Union[ReqItem, _Mapping]]] = ..., language: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class CheckReq(_message.Message):
    __slots__ = ["hash", "language"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    hash: str
    language: str
    def __init__(self, hash: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class Rep(_message.Message):
    __slots__ = ["hash", "items", "location", "sum", "timestamp", "version"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    hash: str
    items: _containers.RepeatedCompositeFieldContainer[RepItem]
    location: str
    sum: float
    timestamp: int
    version: str
    def __init__(self, items: _Optional[_Iterable[_Union[RepItem, _Mapping]]] = ..., hash: _Optional[str] = ..., sum: _Optional[float] = ..., timestamp: _Optional[int] = ..., version: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class RepItem(_message.Message):
    __slots__ = ["accepted", "description", "meta", "name", "parent_type_id", "price_per", "quantity", "type_id"]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    description: str
    meta: _struct_pb2.Struct
    name: str
    parent_type_id: int
    price_per: float
    quantity: float
    type_id: int
    def __init__(self, type_id: _Optional[int] = ..., parent_type_id: _Optional[int] = ..., quantity: _Optional[float] = ..., name: _Optional[str] = ..., price_per: _Optional[float] = ..., description: _Optional[str] = ..., accepted: bool = ..., meta: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ReqItem(_message.Message):
    __slots__ = ["quantity", "type_id"]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    type_id: int
    def __init__(self, type_id: _Optional[int] = ..., quantity: _Optional[int] = ...) -> None: ...
