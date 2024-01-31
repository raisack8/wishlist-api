from typing import TypeVar, Generic
from pydantic.generics import GenericModel

T1 = TypeVar("T1")

class Response(GenericModel, Generic[T1]):
    code: int
    message: str
    data: T1