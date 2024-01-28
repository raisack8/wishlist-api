from pydantic import BaseModel
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.apis import (
    health,
    item,
    saving,
    user,
    file
    )

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://192.168.0.18:3000",
    "http://192.168.0.18:800",
]

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(request.headers)
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

# app.include_router(test_api.router, tags=["tests"])

app.include_router(health.router, tags=["health"])

app.include_router(item.router, tags=["item"])
app.include_router(saving.router, tags=["saving"])
app.include_router(user.router, tags=["user"])
app.include_router(file.router, tags=["file"])