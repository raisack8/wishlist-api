from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select

from ..models.t_saving_history import TSavingHistory
from ..models.t_user import TUser

from ..schemas.requests.saving import PSavingHistory

class SavingCrud:
    def create_saving_table(
            db: AsyncSession, 
            data: PSavingHistory
            ) -> bool:
        try:
            # sub → uuid
            user = db.query(TUser.uuid).filter(
                TUser.sub==data.sub).first()
            # uuid → Saving
            db_amount = TSavingHistory(
                uuid = user[0],
                amount = data.amount,
            )
            db.add(db_amount)
            db.commit()
            db.refresh(db_amount)
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False
        
    def select_saving_table(
            db: AsyncSession, 
            sub: str
        ):
        try:
            items = db.query(
                    TSavingHistory.amount,
                    TSavingHistory.created_at,
                ).filter(
                    TUser.sub == sub
                ).all()
            return items
        except Exception as e:
            print(e)
            db.rollback()
            return []
        
    def select_saving_table_amount(
            db: AsyncSession, 
            sub: str
        ):
        try:
            result = db.execute(
                    select(func.sum(TSavingHistory.amount))
                    .join(TUser, TUser.uuid == TSavingHistory.uuid)  # JOIN条件
                    .filter(TUser.sub == sub)
                )
            total_amount = result.scalar_one_or_none()
            return total_amount if total_amount is not None else 0
        except Exception as e:
            print(e)
            db.rollback()
            return False