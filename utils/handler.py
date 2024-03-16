import hashlib
import re
import secrets
from settings import settings


class PwdHandler:
    @staticmethod
    def pwd_hash(password: str) -> str:
        salted_password = password + settings.ConfigParam.salt
        hashed = hashlib.md5(salted_password.encode())
        return hashed.hexdigest()


class TokenHandler:
    @staticmethod
    def client_access_token() -> str:
        return secrets.token_hex(25)
