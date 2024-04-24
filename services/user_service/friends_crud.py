import datetime
import json
import traceback

from fastapi import APIRouter, Request, Depends
from sqlalchemy import and_
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
                     .filter(Friends.user_id2 == cid, Friends.status == 'friend'))
        friends_2 = (db.query(Friends.user_id2, Users.name, Users.picture).join(Users, Friends.user_id2 == Users.cid)
                     .filter(Friends.user_id1 == cid, Friends.status == 'friend'))
        db.expire_all()
        friends_list_1 = friends_1.all()
        friends_list_2 = friends_2.all()

        friends_list = friends_list_1 + friends_list_2
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
        print(friends_dict, datetime.datetime.now())
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


@router.put('/friend_request/')
def change_friend_status(friend: FriendIDBase, request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        pending_request = db.query(Friends).filter(Friends.user_id1 == friend.cid,
                                                    Friends.user_id2 == cid,
                                                    Friends.status == 'pending').first()
        sent_request = db.query(Friends).filter(Friends.user_id1 == cid,
                                                Friends.user_id2 == friend.cid,
                                                Friends.status == 'pending').first()
        if pending_request and sent_request:
            pending_request.status = 'friend'
            db.commit()
            db.delete(sent_request)
            db.commit()
            return JSONResponse({"msg": "Friend request is accepted"})
        elif not pending_request:
            raise Exception("Friend request is not exist")
        else:
            pending_request.status = 'friend'
            db.commit()
            return JSONResponse({"msg": "Friend request is accepted"})
    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)


@router.delete('/friend_request/')
def refuse_friend_request(friend: FriendIDBase, request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        pending_request = db.query(Friends).filter(Friends.user_id1 == friend.cid,
                                                   Friends.user_id2 == cid,
                                                   Friends.status == 'pending').first()
        sent_request = db.query(Friends).filter(Friends.user_id1 == cid,
                                                Friends.user_id2 == friend.cid,
                                                Friends.status == 'pending').first()
        if pending_request:
            db.delete(pending_request)
            db.commit()
            if sent_request:
                db.delete(sent_request)
                db.commit()
            return JSONResponse({"msg": "Friend request is refused"})
        raise Exception("Friend request is not exist")

    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)


@router.get('/friend_request/')
def get_friend_requests(request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        requests_msg = (db.query(Friends.id, Friends.user_id1, Friends.user_id2, Users.name, Users.email, Users.picture)
                        .join(Users, Friends.user_id1 == Users.cid)
                        .filter(Friends.user_id2 == cid, Friends.status == 'pending')
                        .order_by(Friends.created_at.desc()))
        requests_list = []
        for request in requests_msg:
            request_dict = {
                'id': request[0],
                'from_id': request[1],
                'to_id': request[2],
                'from_name': request[3],
                'from_email': request[4],
                'from_picture': request[5]
            }
            requests_list.append(request_dict)
        return JSONResponse(requests_list)

    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)
