from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    owner_id: int
