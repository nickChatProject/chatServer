import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.users.schemas import UserBase
from settings import settings
from utils.handler import PwdHandler

from models.db_connection.database import get_db
from models.users.users import Users
from redis_cache.connection import RedisCache
from utils.handler import TokenHandler

router = APIRouter()


@router.post("/user_login/")
def user_login(userinfo: UserBase, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.account == userinfo.account).first()
    if not user:
        raise HTTPException(status_code=418, detail="Account does not exist")
    if PwdHandler.pwd_hash(userinfo.password) != user.password:
        raise HTTPException(status_code=418, detail="Incorrect password")
    token = TokenHandler.client_access_token()
    cid = {'cid': user.cid}
    RedisCache.r.set(token, json.dumps(cid), settings.RedisParam.expire_time)
    return {"success": True, "token": token}
