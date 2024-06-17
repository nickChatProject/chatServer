from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    class Database:
        database_url: str = 'mysql+pymysql://'

    class RedisParam:
        url: str = ''
        port: int = 11981
        password: str = ''
        expire_time: int = 60 * 60 * 24

    class ConfigParam:
        salt: str = 'myproject'


class SettingsProd(BaseSettings):
    class Database:
        database_url: str = 'mysql+pymysql://'

    class RedisParam:
        url: str = ''
        port: int = 6379
        password: str = None
        expire_time: int = 60 * 60 * 24

    class ConfigParam:
        salt: str = 'myproject'


if os.getenv('ENV') == 'prod':
    print("production environment")
    settings = SettingsProd()
else:
    print("test environment")
    settings = Settings()
