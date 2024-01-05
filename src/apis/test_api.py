from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union

from ..models.database import get_db
from ..schemas.response.test_schema import PItem
from ..schemas.requests.test_request import PReqData
from ..services.test_service import ItemOperate

router = APIRouter()

@router.get(
        "/",
        summary="Hello Worldを返すだけ"
        )
async def index():
    return {"message": "Hello World"}

@router.get(
        "/item",
        response_model=Union[PItem, list[PItem]],
        description="itemをidで参照。idを指定しなかったら全データ参照",
        )
async def read_item(
    item_id: int = None,
    db: Session = Depends(get_db),
) -> PItem:
    result = ItemOperate.select_item(db, item_id)
    return result

@router.post(
        "/item",
        response_model=None,
        description="itemを登録"
        )
async def register_item(
    item: PReqData, 
    db: Session = Depends(get_db),
) -> None:
    ItemOperate.register_item(db, item)
    pass

@router.put(
        "/item",
        response_model=None,
        description="itemを変更・更新"
        )
async def update_item(
    item_id: str,
    title: str = None,
    description: str = None,
    db: Session = Depends(get_db),
) -> None:
    ItemOperate.update_item(db, item_id, title, description)
    pass

@router.delete(
        "/item",
        response_model=None,
        description="itemを削除"
        )
async def delete_item(
    item_id: str,
    db: Session = Depends(get_db),
) -> None:
    ItemOperate.delete_item(db, item_id)
    pass