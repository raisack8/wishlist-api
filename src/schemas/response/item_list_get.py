from pydantic import BaseModel
from typing import Optional

class GItemGetList(BaseModel):
    id: int
    name: str
    price: int
    category: int
    image_url: Optional[str] = None