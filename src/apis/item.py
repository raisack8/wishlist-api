from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..schemas.requests.item_register import PReqItemRegister
from ..schemas.response.item_list_get import GItemGetList
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
    print(f"item_register, {data.title}, {data.price}, {data.category}, {data.memo},")
    result = ServiceItem.item_register(
        db,
        data
    )
    return result

@router.get(
        "/item/list-get/{sub}",
        response_model=list[GItemGetList],
        # response_model=None,
        description="itemリストを取得",
        )
async def read_item(
    sub: str,
    db: Session = Depends(get_db),
):
    uuid = UserCrud.get_uuid_by_sub(db, sub)
    result = ServiceItem.item_list_get(
        db,
        uuid
    )
    return result