from pydantic import BaseModel
from enum import Enum


class PReqItemRegister(BaseModel):
    sub: str
    title: str
    price: int
    memo: str
    image_url: str


class PReqItemUpdate(BaseModel):
    id: int
    title: str
    price: int
    memo: str
    image_url: str
