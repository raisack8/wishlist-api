from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.item import ItemCrud
from ..schemas.requests.test_request import PReqData
from ..schemas.requests.item_register import PReqItemRegister


class ServiceItem:
    def item_register(
            db: AsyncSession, 
            data: PReqItemRegister
            ):
        return ItemCrud.create_item_table(db, data)
    
    def item_list_get(
            db: AsyncSession, 
            user_id: int
            ):
        items = ItemCrud.select_item_table_list(db, user_id)
        if not items:
            return []
        result = [{
                'id': item.id,
                'name': item.title,
                'price': item.price,
                'category': item.category,
                'image_url': item.image_url or 'default.jpg',
            } for item in items]
        return result
        