from fastapi import APIRouter

from . import users

main_router = APIRouter()
main_router.include_router(users.router)
