from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..services.user import ServiceUser
from ..schemas.requests.user import PLineLoginInfo, PDataReset

router = APIRouter()


@router.post(
    "/user/login-process",
    response_model=None,
    summary="/login-process",
    description="ユーザーログイン処理API",
)
async def login_process(
    data: PLineLoginInfo,
    db: Session = Depends(get_db),
) -> str:
    ServiceUser.login_process(
        db,
        data,
    )

@router.post(
    "/user/data-reset",
    response_model=None,
    summary="/data-reset",
    description="ユーザーデータ削除API",
)
async def data_reset(
    data: PDataReset,
    db: Session = Depends(get_db),
) -> str:
    ServiceUser.data_reset(
        db,
        data.sub,
    )