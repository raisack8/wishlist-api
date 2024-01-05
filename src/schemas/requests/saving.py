from pydantic import BaseModel

class PSavingHistory(BaseModel):
    amount: int

    