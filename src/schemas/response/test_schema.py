from pydantic import BaseModel

class PItem(BaseModel):
    title: str
    description: str