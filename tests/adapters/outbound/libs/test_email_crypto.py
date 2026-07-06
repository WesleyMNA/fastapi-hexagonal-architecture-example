import base64
import hashlib
import hmac
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from src.adapters.outbound.config import crypto_settings


class EmailCrypto:
    @staticmethod
    def hash(email: str) -> str:
        encoded_email = email.encode()
        digest = hmac.new(
            crypto_settings.email_hash_secret_key,
            encoded_email,
            hashlib.sha256
        ).digest()
        return base64.urlsafe_b64encode(digest).decode()

    @staticmethod
    def encrypt(email: str) -> str:
        aesgcm = AESGCM(crypto_settings.email_crypto_secret_key)
        nonce = os.urandom(12)
        data = email.encode()
        encrypted = aesgcm.encrypt(nonce, data, None)
        return base64.urlsafe_b64encode(nonce + encrypted).decode()
