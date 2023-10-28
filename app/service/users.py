from app.db.connection import Dao
from app.db.queries import get_users, get_user, create_user, update_user, delete_user
from fastapi import HTTPException


class Service_user:
    def __init__(self) -> None:
        self.dao = Dao()

    def get_users_from_db(self):
        try:
            users = get_users(self.dao.connect_to_db())
            return users
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error getting users: {err}, service users"
            )

    def get_user_from_db(self, user_id):
        try:
            user = get_user(self.dao.connect_to_db(), user_id)
            return user
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error getting user: {err}, service users"
            )

    def create_user(self, user):
        try:
            user = create_user(self.dao.connect_to_db(), user)
            return user
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error creating user: {err}, service users"
            )

    def update_user(self, user_id, user):
        try:
            user = update_user(self.dao.connect_to_db(), user_id, user)
            return user
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error updating user: {err}, service users"
            )

    def delete_user(self, user_id):
        try:
            value = delete_user(self.dao.connect_to_db(), user_id)
            if value:
                return {"message": "User deleted"}
            else:
                return {"message": "User not deleted"}
        except Exception as err:
            raise HTTPException(
                status_code=500, detail=f"Error deleting user: {err}, service users"
            )   