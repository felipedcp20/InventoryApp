from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User
from app.service.users import Service_user

router = APIRouter()

@router.get("/users", response_model=List[User])
def read_users():
    try:
        service = Service_user()
        users = service.get_users_from_db()
        return users
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error getting users: {err}")
    
