from typing import Protocol


class EmailCryptoProtocol(Protocol):
    def hash(self, email: str) -> str:
        ...

    def encrypt(self, email: str) -> str:
        ...
