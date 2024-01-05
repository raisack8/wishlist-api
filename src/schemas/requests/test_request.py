from pydantic import BaseModel

class PReqData(BaseModel):
    title: str
    description: str