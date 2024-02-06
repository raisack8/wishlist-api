from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.user import UserCrud
from ..schemas.requests.user import PLineLoginInfo


class ServiceUser:
    def login_process(db: AsyncSession, data: PLineLoginInfo):
        UserCrud.login_process(db, data)

    def get_uuid_by_sub(db: AsyncSession, data: PLineLoginInfo):
        return UserCrud.get_uuid_by_sub(db, data)

    def data_reset(db: AsyncSession, sub: str):
        UserCrud.data_reset(db, sub)