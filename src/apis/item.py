from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..schemas.requests.item_register import PReqItemRegister, PReqItemUpdate
from ..schemas.response.item_list_get import GItemGetList, GItemGet
from ..services.item import ServiceItem
from ..services.user import UserCrud

router = APIRouter()

@router.post(
        "/item/register",
        response_model=None,
        description="itemを登録"
        )
async def register_item(
    data: PReqItemRegister,
    db: Session = Depends(get_db),
) -> str:
    result = ServiceItem.item_register(
        db,
        data
    )
    return result

@router.post(
        "/item/update",
        response_model=None,
        description="itemを更新"
        )
async def update_item(
    data: PReqItemUpdate,
    db: Session = Depends(get_db),
) -> str:
    result = ServiceItem.item_update(
        db,
        data
    )
    return result

@router.get(
        "/item/list-get/{sub}",
        response_model=list[GItemGetList],
        description="itemリストを取得",
        )
async def read_item(
    sub: str,
    db: Session = Depends(get_db),
):
    result = ServiceItem.item_list_get(
        db,
        sub
    )
    return result

@router.get(
        "/item/get/{item_id}",
        response_model=GItemGet,
        description="特定のアイテムを取得",
        )
async def read_item(
    item_id: str,
    db: Session = Depends(get_db),
):
    result = ServiceItem.item_get(
        db,
        item_id
    )
    return result