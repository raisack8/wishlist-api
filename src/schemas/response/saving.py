import datetime
from pydantic import BaseModel

class GSavingHistoryList(BaseModel):
    amount: int
    created_at: datetime.datetime