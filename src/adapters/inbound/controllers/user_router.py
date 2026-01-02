from typing import List

from fastapi import APIRouter, Depends, Response
from starlette import status

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


@router.post('', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create(
        user: User = Depends(mapper.from_create_req),
        service: UserService = Depends(create_user_service)
):
    return await service.create(user)


@router.put('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(
        user_id: int,
        user: User = Depends(mapper.from_create_req),
        service: UserService = Depends(create_user_service)
):
    await service.update(user_id, user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def patch(
        user_id: int,
        user: User = Depends(mapper.from_patch_req),
        service: UserService = Depends(create_user_service)
):
    await service.patch(user_id, user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        user_id: int,
        service: UserService = Depends(create_user_service)
):
    await service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
