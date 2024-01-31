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
    summary="/history",
    description="貯金額登録API",
)
async def saving_history(
    data: PSavingHistory,
    db: Session = Depends(get_db),
) -> str:
    result = ServiceSaving.saving_history(db, data)
    return f"item_register, {result}"


@router.get(
    "/saving/history_get/{sub}",
    response_model=list[GSavingHistoryList],
    summary="/history_get/{sub}",
    description="貯金歴一覧取得API",
)
async def get_saving_history_list(
    sub: str,
    db: Session = Depends(get_db),
):
    result = ServiceSaving.get_saving_history_list(db, sub)
    return result


@router.get(
    "/saving/amount/{sub}",
    response_model=int,
    summary="/amount/{sub}",
    description="貯金合計額取得API",
)
async def get_saving_amount(
    sub: str,
    db: Session = Depends(get_db),
):
    result = ServiceSaving.get_saving_amount(db, sub)
    return result if result else 0
