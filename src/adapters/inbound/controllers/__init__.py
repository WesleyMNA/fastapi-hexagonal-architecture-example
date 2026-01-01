from fastapi import APIRouter

from . import user

main_router = APIRouter()
main_router.include_router(users.router)
