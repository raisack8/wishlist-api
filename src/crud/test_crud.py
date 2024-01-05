from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from ..models.test_model import Item

from ..schemas.requests.test_request import PReqData

class ItemCrud:
    def select_items(
            db: AsyncSession, 
            item_id: int = None
            ) -> None:
        if item_id:
            item = db.query(Item).filter(Item.id == item_id).first()
            return item
        item = db.query(Item).all()
        return item
    
    def create_items(
            db: AsyncSession, 
            item: PReqData
            ) -> None:
        try:
            db_item = Item(
                title = item.title,
                description = item.description,
            )
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            return None
        except IntegrityError:
            return None
        
    def update_items(
            db: AsyncSession, 
            item_id: int,
            title: str = None,
            description: str = None
            ) -> None:
        item = db.query(Item).filter(Item.id == item_id).first()
        item.title = title
        item.description = description
        db.add(item)
        db.commit()
        db.refresh(item)
        return None
    
    def delete_items(
            db: AsyncSession, 
            item_id: int,
            ) -> None:
        try:
            item = db.query(Item).filter(Item.id == item_id).first()
            db.delete(item)
            db.commit()
            return None
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()