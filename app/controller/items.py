from fastapi import APIRouter, HTTPException
from typing import List
from app.models.item import Item
from app.service.items import Service_items

router = APIRouter()


@router.get("/items", response_model=List[Item])
def read_users():
    try:
        service = Service_items()
        users = service.get_items_from_db()
        return users
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error getting items: {err}")