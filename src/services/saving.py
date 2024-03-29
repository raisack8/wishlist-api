from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.saving import SavingCrud
from ..schemas.requests.saving import PSavingHistory


class ServiceSaving:
    def saving_history(db: AsyncSession, data: PSavingHistory):
        return SavingCrud.create_saving_table(db, data)

    def get_saving_history_list(db: AsyncSession, sub: str):
        return SavingCrud.select_saving_table(db, sub)

    def get_saving_amount(db: AsyncSession, sub: str):
        return SavingCrud.select_saving_table_amount(db, sub)
