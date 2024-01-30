from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..services.user import ServiceUser
from ..schemas.requests.user import PLineLoginInfo

router = APIRouter()


@router.post(
    "/user/login-process", response_model=None, description="ユーザーログイン処理"
)
async def login_process(
    data: PLineLoginInfo,
    db: Session = Depends(get_db),
) -> str:
    ServiceUser.login_process(
        db,
        data,
    )
