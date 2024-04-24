import json
import traceback

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse, JSONResponse, FileResponse

from redis_cache.connection import RedisCache
from services.file_service import image_handler, file_handler
from services.user_service import crud, auth, friends_crud
from services.chat_service import chat_handler
from services.ws_service import websocket

app = FastAPI()
RedisCache().redis_connect()


class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            if (request.url.path == '/user_login/'
                    or request.url.path == '/image/'
                    or request.url.path.startswith('/docs'))\
                    or request.url.path.startswith('/openapi'):
                return await call_next(request)
            token = request.headers.get("Authorization")
            cid_info = RedisCache.r.get(token)
            if token and cid_info:
                cid = json.loads(cid_info)['cid']
                cid_bytes = str(cid).encode('utf-8')
                headers = dict(request.scope['headers'])
                headers[b'cid'] = cid_bytes
                request.scope['headers'] = [(k, v) for k, v in headers.items()]
                return await call_next(request)
            else:
                raise Exception("User does not login or token is expired.")
        except Exception as e:
            err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
            return JSONResponse(err_res, status_code=418)


origins = ["*"]

app.add_middleware(MyMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crud.router)
app.include_router(auth.router)
app.include_router(chat_handler.router)
app.include_router(friends_crud.router)
app.include_router(image_handler.router)
app.include_router(file_handler.router)
app.include_router(websocket.router)




