from typing import List

from fastapi import APIRouter, Depends

import src.adapters.inbound.mappers.user_dto_mapper as mapper
from src.adapters.inbound.dtos import UserResponse
from src.config import create_user_service
from src.domain import User
from src.ports.inbound.services import UserService

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('', response_model=List[UserResponse])
async def find_all(service: UserService = Depends(create_user_service)):
    return await service.find_all()


@router.get('/{user_id}', response_model=UserResponse)
async def find_by_id(user_id: int, service: UserService = Depends(create_user_service)):
    return await service.find_by_id(user_id)


@router.post('', response_model=UserResponse)
async def create(
        user: User = Depends(mapper.from_create_req),
        service: UserService = Depends(create_user_service)
):
    return await service.create(user)
