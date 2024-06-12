import redis

from app.settings import settings


class RedisCache:
    r = None

    @classmethod
    def redis_connect(cls):
        try:
            print(settings.RedisParam.url, settings.RedisParam.password)
            cls.r = redis.Redis(
                host=settings.RedisParam.url,
                port=settings.RedisParam.port,
                password=settings.RedisParam.password)

        except Exception as e:
            print(e)
