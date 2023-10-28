from app.db.connection import Dao
from fastapi import HTTPException
from app.db.queries import get_items


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