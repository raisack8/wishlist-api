from pydantic import BaseModel
from typing import Optional


class GItemGetList(BaseModel):
    id: int
    name: str
    price: int
    category: int
    image_url: Optional[str] = None
    memo: str


class GItemGet(BaseModel):
    id: int
    name: str
    price: int
    category: int
    image_file_name: str
    image_url: Optional[str] = None
    memo: str
