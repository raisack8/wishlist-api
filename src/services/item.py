import os
from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.item import ItemCrud
from ..schemas.requests.test_request import PReqData
from ..schemas.requests.item_register import PReqItemRegister, PReqItemUpdate
from ..services.file import ServiceFile


class ServiceItem:
    def item_register(db: AsyncSession, data: PReqItemRegister):
        return ItemCrud.create_item_table(db, data)

    def item_update(db: AsyncSession, data: PReqItemUpdate):
        return ItemCrud.update_item_table(db, data)

    def item_list_get(db: AsyncSession, sub: str):
        items = ItemCrud.select_item_table_list(db, sub)
        if not items:
            return []
        result = [
            {
                "id": item.id,
                "name": item.title,
                "price": item.price,
                "image_url": item.image_url or "default.jpg",
                "memo": item.memo,
            }
            for item in items
        ]
        return result

    def item_get(db: AsyncSession, item_id: str):

        item = ItemCrud.select_item(db, item_id)
        file_path = os.path.join(os.getcwd(), r"resources")
        data = {
            "id": item.id,
            "name": item.title,
            "price": item.price,
            "image_file_name": item.image_url,
            "image_url": ServiceFile.image_convert_to_binari(file_path, item.image_url),
            "memo": item.memo,
        }
        return data

    def item_delete(db: AsyncSession, item_id: str):
        return ItemCrud.delete_item(db, item_id)

    def item_purchase(db: AsyncSession, item_id: str, sub: str):
        return ItemCrud.purchase_item(db, item_id, sub)
