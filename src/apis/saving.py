from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..schemas.requests.saving import PSavingHistory
from ..schemas.response.saving import GSavingHistoryList
from ..services.saving import ServiceSaving
from ..services.user import UserCrud

router = APIRouter()

@router.post(
        "/saving/history",
        response_model=None,
        description="貯金額を登録"
        )
async def saving_history(
    data: PSavingHistory,
    db: Session = Depends(get_db),
) -> str:
    result = ServiceSaving.saving_history(
        db,
        data
    )
    return f"item_register, {result}"

@router.get(
        "/saving/history_get/{user_id}",
        response_model=list[GSavingHistoryList],
        description="貯金歴を取得",
        )
async def get_saving_history_list(
    user_id: int,
    db: Session = Depends(get_db),
):
    result = ServiceSaving.get_saving_history_list(
        db,
        user_id
    )
    return result

@router.get(
        "/saving/amount/{sub}",
        response_model=int,
        description="合計貯金額を取得",
        )
async def get_saving_amount(
    sub: str,
    db: Session = Depends(get_db),
):
    uuid = UserCrud.get_uuid_by_sub(db, sub)
    result = ServiceSaving.get_saving_amount(
        db,
        uuid
    )
    return result if result else 0