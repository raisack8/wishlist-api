from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from ..models.t_wishlist import TWishlist
from ..models.t_user import TUser

from ..schemas.requests.test_request import PReqData
from ..schemas.requests.item_register import PReqItemRegister, PReqItemUpdate


class ItemCrud:
    def create_item_table(db: AsyncSession, data: PReqItemRegister) -> None:
        try:
            # sub → uuid
            user = db.query(TUser.uuid).filter(TUser.sub == data.sub).first()
            # uuid → items
            db_item = TWishlist(
                uuid=user[0],
                title=data.title,
                price=data.price,
                memo=data.memo,
                image_url=data.image_url,
            )
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def update_item_table(db: AsyncSession, data: PReqItemUpdate) -> bool:
        try:
            result = db.execute(select(TWishlist).filter(TWishlist.id == data.id))
            wish_list = result.scalar_one_or_none()
            if wish_list:
                wish_list.title = data.title
                wish_list.price = data.price
                wish_list.memo = data.memo
                wish_list.image_url = data.image_url
                db.commit()
                return True
            else:
                raise Exception("Item not found")
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def select_item_table_list(db: AsyncSession, sub: int):
        try:
            items = db.query(
                TWishlist.id,
                TWishlist.title,
                TWishlist.price,
                TWishlist.image_url,
                TWishlist.memo,
            ).join(TUser, TUser.sub == sub)[:10]
            return items
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def select_item(db: AsyncSession, item_id: str):
        try:
            item = (
                db.query(
                    TWishlist.id,
                    TWishlist.title,
                    TWishlist.price,
                    TWishlist.image_url,
                    TWishlist.memo,
                )
                .filter(TWishlist.id == item_id)
                .first()
            )
            return item
        except Exception as e:
            print(e)
            db.rollback()
            return False
