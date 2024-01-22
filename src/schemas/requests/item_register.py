from pydantic import BaseModel
from enum import Enum

class ECategory(int, Enum):
    THINGS = 1
    TRIP = 2

class PReqItemRegister(BaseModel):
    sub: str
    title: str
    price: int
    category: ECategory
    memo: str