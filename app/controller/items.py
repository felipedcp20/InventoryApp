from fastapi import APIRouter, HTTPException
from typing import List
from app.models.item import Item
from app.service.items import Service_items

router = APIRouter()


@router.get("/items", response_model=List[Item], tags=["items"])
def read_items():
    try:
        service = Service_items()
        users = service.get_items_from_db()
        return users
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error getting items: {err}")
    
@router.get("/item/{item_id}", response_model=Item, tags=["items"])
def read_item(item_id: int):
    try:
        service = Service_items()
        item = service.get_item_from_db(item_id)
        return item
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error getting item: {err}")
    
@router.post("/item", response_model=Item, tags=["items"])
def create_item(item: Item):
    try:
        service = Service_items()
        item = service.create_item(item)
        return {"message": "Item created successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error creating item: {err}")
    
@router.put("/item/{item_id}", response_model=Item, tags=["items"])
def update_item(item_id: int, item: Item):
    try:
        service = Service_items()
        item = service.update_item(item_id, item)
        return {"message": "Item updated successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error updating item: {err}")
    
@router.delete("/item/{item_id}", response_model=Item, tags=["items"])
def deleted_item(item_id: int):
    try:
        service = Service_items()
        item = service.deleted_item(item_id)
        return {"message": "Item deleted successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error deleting item: {err}")