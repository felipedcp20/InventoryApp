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


@router.get("/user/{user_id}", response_model=User)
def read_user(user_id: int):
    try:
        service = Service_user()
        user = service.get_user_from_db(user_id)
        return user
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error getting user: {err}")


@router.post("/user", response_model=User)
def create_user(user: User):
    try:
        service = Service_user()
        user = service.create_user(user)
        return {"message": "User created successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error creating user: {err}")


@router.put("/user/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    try:
        service = Service_user()
        user = service.update_user(user_id, user)
        return {"message": "User updated successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error updating user: {err}")
