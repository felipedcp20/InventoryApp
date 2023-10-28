from fastapi import APIRouter, HTTPException
from typing import List
from app.models.item import Item

router = APIRouter()


@router.get("/items")
def read_users():
    print("items")
