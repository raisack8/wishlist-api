from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func

from ..models.t_saving_history import TSavingHistory

from ..schemas.requests.saving import PSavingHistory

class SavingCrud:
    def create_saving_table(
            db: AsyncSession, 
            data: PSavingHistory
            ) -> None:
        try:
            db_amount = TSavingHistory(
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
            user_id: int
        ):
        try:
            items = db.query(
                    TSavingHistory.amount,
                    TSavingHistory.created_at,
                ).filter(
                    TSavingHistory.user_id == user_id
                ).all()
            return items
        except Exception as e:
            print(e)
            db.rollback()
            return False
        
    def select_saving_table_amount(
            db: AsyncSession, 
            user_id: int
        ):
        try:
            total_amount = db.query(
                    func.sum(TSavingHistory.amount)
                ).filter(
                    TSavingHistory.user_id == user_id
                ).scalar()
            return total_amount
        except Exception as e:
            print(e)
            db.rollback()
            return False