from pydantic_settings import BaseSettings


class CryptoSettings(BaseSettings):
    email_secret_key: bytes = b'153eb1f9f68c83b203f2c39ea1311fc69640af116ddc0572921a261f18a3a16b'


crypto_settings = CryptoSettings()
