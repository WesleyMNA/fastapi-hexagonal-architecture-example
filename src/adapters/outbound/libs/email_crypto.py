import hmac
import hashlib
import base64

from src.adapters.outbound.config import crypto_settings


class EmailCrypto:
    @staticmethod
    def hash(email: str) -> str:
        encoded_email = email.encode()
        digest = hmac.new(
            crypto_settings.email_secret_key,
            encoded_email,
            hashlib.sha256
        ).digest()
        return base64.urlsafe_b64encode(digest).decode()

    @staticmethod
    def encrypt(email: str) -> str:
        return email
