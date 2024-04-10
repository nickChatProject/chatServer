import json
import traceback

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from models.users.schemas import UserBase, Token
from settings import settings
from utils.handler import PwdHandler

from models.db_connection.database import get_db
from models.users.users import Users
from redis_cache.connection import RedisCache
from utils.handler import TokenHandler

router = APIRouter()


@router.post("/user_login/")
def user_login(userinfo: UserBase, db: Session = Depends(get_db)):
    try:
        user = db.query(Users).filter(Users.account == userinfo.account).first()
        if not user:
            raise Exception('Account does not exist')
        if PwdHandler.pwd_hash(userinfo.password) != user.password:
            raise Exception('Incorrect password')
        token = TokenHandler.client_access_token()
        cid = {'cid': user.cid}
        RedisCache.r.set(token, json.dumps(cid), settings.RedisParam.expire_time)
        picture = user.picture if user.picture else ""
        res = {'success': True, 'token': token, 'user_id': user.cid, 'picture': picture}
        return JSONResponse(res)
    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)


@router.post("/user_status_check/")
def user_status_check(token: Token):
    try:
        is_exist = RedisCache.r.get(str(token.token))
        if not is_exist:
            raise Exception('User does not login or token is expired')
        cid = json.loads(is_exist)['cid']
        res = {'user_id': cid}
        return JSONResponse(res)
    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)
