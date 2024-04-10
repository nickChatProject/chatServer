import json
import traceback

from fastapi import APIRouter, Request, Depends
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from models.chats.mssages import Msg
from models.db_connection.database import get_db
from models.users.schemas import UserNameBase, FriendIDBase
from models.users.users import Users, Friends

router = APIRouter()


@router.get('/friends/')
def get_friends(request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        friends_1 = (db.query(Friends.user_id1, Users.name, Users.picture).join(Users, Friends.user_id1 == Users.cid)
                     .filter(Friends.user_id2 == cid, Friends.status == 'friend').all())
        friends_2 = (db.query(Friends.user_id2, Users.name, Users.picture).join(Users, Friends.user_id2 == Users.cid)
                     .filter(Friends.user_id1 == cid, Friends.status == 'friend').all())
        friends_list = friends_1 + friends_2
        if len(friends_list) == 0:
            return JSONResponse({'friends': []})
        friends_dict = {"friends": []}
        for friend in friends_list:
            last_message = (db.query(Msg.content, Msg.type, Msg.created_at, Msg.sender_id)
                            .filter(and_(Msg.sender_id == cid, Msg.receiver_id == friend[0]) |
                                    and_(Msg.sender_id == friend[0], Msg.receiver_id == cid))
                            .order_by(Msg.created_at.desc()).first())
            if last_message:
                f = [i for i in friend] + [last_message[0], last_message[1], str(round(last_message[2].timestamp())),
                                           str(last_message[3])]
                friends_dict["friends"].append(f)
            else:
                f = [i for i in friend] + [""] + [""]
                friends_dict["friends"].append(f)
        return JSONResponse(friends_dict)

    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)


@router.post('/friends_by_name/')
def get_friends_by_name(user_name: UserNameBase, request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        friends_1 = (db.query(Friends.user_id1, Users.name, Users.picture).join(Users, Friends.user_id1 == Users.cid)
                     .filter(Friends.user_id2 == cid, Friends.status == 'friend', Users.name == user_name.name).all())
        friends_2 = (db.query(Friends.user_id2, Users.name, Users.picture).join(Users, Friends.user_id2 == Users.cid)
                     .filter(Friends.user_id1 == cid, Friends.status == 'friend', Users.name == user_name.name).all())
        friends_list = friends_1 + friends_2
        if len(friends_list) == 0:
            raise Exception('No friends found, please add friends before getting friends')
        friends_dict = {"friends": []}
        for friend in friends_list:
            f = [i for i in friend]
            friends_dict["friends"].append(f)
        return JSONResponse(friends_dict)

    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)


@router.put('/friends/')
def change_friend_status(friend: FriendIDBase, request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        db.query(Friends).filter(and_(Friends.user_id1 == cid, Friends.user_id2 == friend.cid |
                                      and_(Friends.user_id1 == friend.cid, Friends.user_id2 == cid))).update(
            {'status': 'friend'})
        db.commit()
        return JSONResponse({"msg", "Friend request is accepted"})

    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)
