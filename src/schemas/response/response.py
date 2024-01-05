'''

使ってない

'''


from enum import Enum
from pydantic import BaseModel
from typing import Any

class ResponseStatus(Enum):
    OK = "OK"
    WARN = "WARN"
    NG = "NG"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"

class ResponseCode(Enum):
    OK = 200
    INTERNAL_ERROR = 500

class BaseResponse(BaseModel):
    status: ResponseStatus = ResponseStatus.OK
    code: ResponseCode = ResponseCode.OK

def resultJson(
        data: Any,
        status: ResponseStatus = ResponseStatus.OK,
        code: ResponseCode = ResponseCode.OK
        ):
    result = {
        "data": data,
        "status": status,
        "code": code
    }

    return result