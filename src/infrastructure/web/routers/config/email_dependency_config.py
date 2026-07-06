from typing import Annotated

from fastapi.params import Depends

from src.domain.shared import EmailCryptoProtocol
from src.infrastructure.libs import EmailCrypto


async def get_email_crypto() -> EmailCryptoProtocol:
    return EmailCrypto()


EmailCryptoDep = Annotated[EmailCryptoProtocol, Depends(get_email_crypto)]
