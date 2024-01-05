from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.test_crud import ItemCrud
from ..schemas.requests.test_request import PReqData

class ItemOperate:
    def select_item(
            db: AsyncSession, 
            item_id: int = None
            ):
        return ItemCrud.select_items(db, item_id)


    def register_item(
            db: AsyncSession, 
            item: PReqData
            ):
        return ItemCrud.create_items(db, item)
    
    def update_item(
            db: AsyncSession, 
            item_id: int = None,
            title: str = None,
            description: str = None
            ):
        if not item_id or (not title and not description):
            return None
        return ItemCrud.update_items(db, item_id, title, description)
    
    def delete_item(
            db: AsyncSession, 
            item_id: int = None,
            ):
        return ItemCrud.delete_items(db, item_id)
        