from app.db.connection import Dao 
from app.db.queries import get_users
from fastapi import HTTPException

class user:
    def __init__(self) -> None:
        self.dao = Dao()

    def get_users(self):
        try:
            users = get_users(self.dao)
            return users
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Error getting users: {err}, service users")