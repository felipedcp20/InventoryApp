from fastapi import APIRouter, HTTPException
from typing import List
from app.models.models import User
from app.service.users import get_users

router = APIRouter()

@router.get("/users", response_model=List[User])
def read_users():
    try:
        users = get_users()
        return users
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error getting users: {err}")
    
