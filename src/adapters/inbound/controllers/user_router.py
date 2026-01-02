from typing import List

from fastapi import APIRouter, Depends

import src.adapters.inbound.mappers.user_dto_mapper as mapper
from src.adapters.inbound.dtos.user_dtos import UserResponse
from src.config import create_user_service
from src.domain.models.user import User
from src.ports.inbound.services.user_service import UserService

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('', response_model=List[UserResponse])
def get_users(service: UserService = Depends(create_user_service)):
    r = service.find_all()
    return r


@router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, service: UserService = Depends(create_user_service)):
    return service.find_by_id(user_id)


@router.post('', response_model=UserResponse)
def create_user(
        user: User = Depends(mapper.from_create_req),
        service: UserService = Depends(create_user_service)
):
    return service.create(user)
