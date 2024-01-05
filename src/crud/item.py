from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from ..models.t_wishlist import TWishlist

from ..schemas.requests.test_request import PReqData
from ..schemas.requests.item_register import PReqItemRegister, ECategory

class ItemCrud:
    def create_item_table(
            db: AsyncSession, 
            data: PReqItemRegister
            ) -> None:
        try:
            db_item = TWishlist(
                title = data.title,
                price = data.price,
                category = data.category,
                memo = data.memo,
            )
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False
        
    def select_item_table_list(
            db: AsyncSession, 
            user_id: int
            ):
        try:
            items = db.query(
                    TWishlist.id,
                    TWishlist.title,
                    TWishlist.price,
                    TWishlist.category,
                    TWishlist.image_url,
                ).filter(
                    TWishlist.user_id == user_id
                )[:10]
            return items
        except Exception as e:
            print(e)
            db.rollback()
            return False
    