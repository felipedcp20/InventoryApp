from fastapi import APIRouter, HTTPException
from typing import List
from app.models.models import Item

router = APIRouter()

@router.get("/items")
def read_users():
    print("items")
       

