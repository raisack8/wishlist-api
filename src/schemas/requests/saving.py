from pydantic import BaseModel

class PSavingHistory(BaseModel):
    sub: str
    amount: int

    