from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..schemas.requests.item_register import (
    PReqItemRegister,
    PReqItemUpdate,
    PReqItemDelete,
    PReqItemPurchase,
)
from ..schemas.response.item_list_get import GItemGetList, GItemGet
from ..services.item import ServiceItem
from ..services.user import UserCrud

router = APIRouter()


@router.post(
    "/item/register",
    response_model=None,
    summary="/register",
    description="ITEM登録API",
)
async def item_register(
    data: PReqItemRegister,
    db: Session = Depends(get_db),
) -> str:
    result = ServiceItem.item_register(db, data)
    return result


@router.post(
    "/item/update", response_model=None, summary="/update", description="ITEM更新API"
)
async def item_update(
    data: PReqItemUpdate,
    db: Session = Depends(get_db),
) -> str:
    result = ServiceItem.item_update(db, data)
    return result


@router.get(
    "/item/list-get/{sub}",
    response_model=list[GItemGetList],
    summary="/list-get/{sub}",
    description="ITEMリスト表示API",
)
async def item_list_get_by_sub(
    sub: str,
    db: Session = Depends(get_db),
):
    result = ServiceItem.item_list_get(db, sub)
    return result


@router.get(
    "/item/get/{item_id}",
    response_model=GItemGet,
    summary="/get/{item_id}",
    description="ITEM詳細情報API",
)
async def item_get_bt_item_id(
    item_id: str,
    db: Session = Depends(get_db),
):
    result = ServiceItem.item_get(db, item_id)
    return result


@router.post(
    "/item/delete",
    response_model=bool,
    summary="/delete",
    description="ITEM削除API",
)
async def item_delete_bt_item_id(
    data: PReqItemDelete,
    db: Session = Depends(get_db),
):
    item_delete_flg = ServiceItem.item_delete(db, data.id)
    return item_delete_flg


@router.post(
    "/item/purchase",
    response_model=None,
    summary="/purchase",
    description="ITEM購入API",
)
async def item_purchase_by_item_id(
    data: PReqItemPurchase,
    db: Session = Depends(get_db),
):
    item_delete_flg = ServiceItem.item_purchase(db, data.id, data.sub)
    return None
