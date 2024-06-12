from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    class Database:
        database_url: str = 'mysql+pymysql://root:a0995102@localhost:3306/py_practice'

    class RedisParam:
        url: str = 'redis-11981.c294.ap-northeast-1-2.ec2.cloud.redislabs.com'
        port: int = 11981
        password: str = 'wdO1yc36yugvXDbc4YYy91wQuICfmec7'
        expire_time: int = 60 * 60 * 24

    class ConfigParam:
        salt: str = 'myproject'


class SettingsProd(BaseSettings):
    class Database:
        database_url: str = 'mysql+pymysql://admin:a0995102@mychatdb.c7442msioygz.ap-northeast-3.rds.amazonaws.com:3306/mychat'

    class RedisParam:
        url: str = 'nick-chat-cache.l1h19d.ng.0001.apn3.cache.amazonaws.com'
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
