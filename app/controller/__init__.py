from fastapi import APIRouter
from app.controller import users, items

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(items.router, prefix="/items", tags=["items"])
