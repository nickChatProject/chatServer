from pydantic_settings import BaseSettings


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


settings = Settings()
