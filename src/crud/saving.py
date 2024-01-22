from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func

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
            total_amount = db.query(
                    func.sum(TSavingHistory.amount)
                ).filter(
                    TUser.sub == sub
                ).scalar()
            return total_amount
        except Exception as e:
            print(e)
            db.rollback()
            return False