from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apis import (
    health,
    item,
    saving
    )

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://192.168.0.18:3000",
]

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# app.include_router(test_api.router, tags=["tests"])

app.include_router(health.router, tags=["health"])

app.include_router(item.router, tags=["item"])
app.include_router(saving.router, tags=["saving"])