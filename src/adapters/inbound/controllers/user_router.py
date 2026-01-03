from typing import List

from fastapi import APIRouter, Response
from starlette import status

from src.adapters.inbound.dtos import UserResponse
from src.adapters.inbound.mappers import UserRequestDep, UserPatchDep
from src.config import UserServiceDep

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('', response_model=List[UserResponse])
async def find_all(service: UserServiceDep):
    return await service.find_all()


@router.get('/{user_id}', response_model=UserResponse)
async def find_by_id(user_id: int, service: UserServiceDep):
    return await service.find_by_id(user_id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create(
        user: UserRequestDep,
        service: UserServiceDep,
):
    return await service.create(user)


@router.put('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update(
        user_id: int,
        user: UserRequestDep,
        service: UserServiceDep,
):
    await service.update(user_id, user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def patch(
        user_id: int,
        user: UserPatchDep,
        service: UserServiceDep,
):
    await service.patch(user_id, user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        user_id: int,
        service: UserServiceDep
):
    await service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
