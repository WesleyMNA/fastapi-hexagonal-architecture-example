from typing import Annotated

from fastapi.params import Depends

from src.adapters.outbound import UserSqlAlchemyRepository
from src.adapters.outbound.libs import EmailCrypto
from src.application import UserService, UserValidator
from src.ports.inbound import UserServiceProtocol, UserValidatorProtocol
from src.ports.outbound import UserRepositoryProtocol, EmailCryptoProtocol

UserRepositoryDep = Annotated[UserRepositoryProtocol, Depends(UserSqlAlchemyRepository)]


async def get_user_validator(r: UserRepositoryDep) -> UserValidatorProtocol:
    return UserValidator(r)


UserValidatorDep = Annotated[UserValidatorProtocol, Depends(get_user_validator)]


async def get_email_crypto() -> EmailCryptoProtocol:
    return EmailCrypto()


EmailCryptoDep = Annotated[EmailCryptoProtocol, Depends(get_email_crypto)]


async def get_user_service(
        r: UserRepositoryDep,
        v: UserValidatorDep,
        c: EmailCryptoDep,
) -> UserServiceProtocol:
    return UserService(r, v, c)


UserServiceDep = Annotated[UserServiceProtocol, Depends(get_user_service)]
