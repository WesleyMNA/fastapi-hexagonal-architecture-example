from typing import List

from fastapi import APIRouter, Depends, HTTPException

import src.adapters.inbound.mappers.user as mapper
from src.adapters.inbound.dtos.user import UserResponse
from src.config.repositories import create_user_repository
from src.domain.models.user import User
from src.ports.outbound.repositories.user import UserRepository

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('', response_model=List[UserResponse])
def get_users(repository: UserRepository = Depends(create_user_repository)):
    return repository.find_all()


@router.get('{user_id}', response_model=UserResponse)
def get_user(user_id: int, repository: UserRepository = Depends(create_user_repository)):
    user = repository.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.post('', response_model=UserResponse)
def create_user(
        user: User = Depends(mapper.from_create_req),
        repository: UserRepository = Depends(create_user_repository)
):
    return repository.create(user)
