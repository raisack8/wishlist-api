from pydantic import BaseModel


class PLineLoginInfo(BaseModel):
    sub: str
    name: str
    picture: str

class PDataReset(BaseModel):
    sub: str