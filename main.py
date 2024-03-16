from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse

from redis_cache.connection import RedisCache
from services.user_service import crud, auth

app = FastAPI()
RedisCache().redis_connect()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crud.router)
app.include_router(auth.router)


@app.get("/image")
def main():
    def iterfiles():  #
        with open('images/logout.png', mode="rb") as file_like:  #
            yield from file_like  #

    return StreamingResponse(iterfiles(), media_type="image/png")
