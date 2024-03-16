import redis

from settings import settings


class RedisCache:
    r = None

    @classmethod
    def redis_connect(cls):
        try:
            cls.r = redis.Redis(
                host=settings.RedisParam.url,
                port=settings.RedisParam.port,
                password=settings.RedisParam.password)

        except Exception as e:
            print(e)
