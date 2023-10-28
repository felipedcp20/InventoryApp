from app.db.connection import Dao
from fastapi import HTTPException
from app.db.queries import get_items, get_item, create_item, update_item, deleted_item


class Service_items:
    def __init__(self) -> None:
        self.dao = Dao()

    def get_items_from_db(self):
        try:
            items = get_items(self.dao.connect_to_db())
            return items
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error getting items: {err}, service items"
            )
        
    def get_item_from_db(self, item_id):
        try:
            item = get_item(self.dao.connect_to_db(), item_id)
            return item
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error getting item: {err}, service items"
            )
        
    def create_item(self, item):
        try:
            item = create_item(self.dao.connect_to_db(), item)
            return item
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error creating item: {err}, service items"
            )
        
    def update_item(self, item_id, item):
        try:
            item = update_item(self.dao.connect_to_db(), item_id, item)
            return item
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error updating item: {err}, service items"
            )
        
    def deleted_item(self, item_id):
        try:
            item = deleted_item(self.dao.connect_to_db(), item_id)
            if item:
                return {"message": "Item deleted successfully"}
            else: 
                raise HTTPException(
                    status_code=404, detail=f"Item not found"
                )
            
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error deleting item: {err}, service items"
            )