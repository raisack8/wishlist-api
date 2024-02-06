import datetime
from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.dialects.postgresql import insert

from ..models.t_user import TUser
from ..models.t_saving_history import TSavingHistory
from ..models.t_wishlist import TWishlist

from ..schemas.requests.user import PLineLoginInfo


class UserCrud:
    def login_process(db: AsyncSession, data: PLineLoginInfo) -> None:
        try:
            stmt = insert(TUser).values(
                sub=data.sub,
                name=data.name,
                picture=data.picture,
                uuid=str(uuid4()),
                last_login_at=datetime.datetime.now(),
                gender=0,
                first_page_id="",
            )
            on_conflict_stmt = stmt.on_conflict_do_update(
                index_elements=["sub"],
                set_=dict(
                    name=data.name,
                    picture=data.picture,
                    last_login_at=datetime.datetime.now(),
                ),
            )
            db.execute(on_conflict_stmt)
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def get_uuid_by_sub(db: AsyncSession, sub: str) -> None:
        try:
            uuid = db.query(TUser.uuid).filter(TUser.sub == sub).first()
            return uuid[0]
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def data_reset(db: AsyncSession, sub: str) -> None:
        try:
            user = db.query(TUser).filter(TUser.sub == sub).first()
            item = delete(TWishlist).where(TWishlist.uuid == user.uuid)
            saving = delete(TSavingHistory).where(TSavingHistory.uuid == user.uuid)
            db.execute(item)
            db.execute(saving)
            db.delete(user)
            db.commit()
            db.close()
        except Exception as e:
            print(e)
            db.rollback()