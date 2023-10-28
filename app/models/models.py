from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    full_name: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    role: Optional[str] = 'empleado'

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    owner_id: int