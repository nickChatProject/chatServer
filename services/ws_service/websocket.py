import json
from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket
from sqlalchemy.orm import Session
from sqlalchemy import and_
from models.db_connection.database import get_db
from datetime import datetime, timezone

from models.chats.mssages import Msg
from models.users.users import Friends

router = APIRouter()
connected_users = {}


@router.websocket("/ws/{user_id}/")
async def websocket_endpoint(user_id, websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    user_id = int(user_id)
    connected_users[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_json()
            print(data)
            print(connected_users)
            # Send the received data to the other user
            msg = dict(data)
            if (msg["type"] == "message" and msg['content'].strip()) or (msg["type"] == "file"):
                # Save message to database
                db_msg = Msg(type=msg['type'], sender_id=msg['sender_id'], receiver_id=msg['receiver_id'],
                             content=msg['content'], created_at=datetime.now(timezone.utc))
                db.add(db_msg)
                db.commit()
                db.refresh(db_msg)

            elif msg["type"] == "friend_request":
                db_friend = db.query(Friends.id, Friends.status).filter(
                    and_(Friends.user_id1 == msg['sender_id'], Friends.user_id2 == msg['receiver_id']) |
                    and_(Friends.user_id1 == msg['receiver_id'], Friends.user_id2 == msg['sender_id']).all())
                if not db_friend:
                    add_friend = Friends(user_id1=msg['sender_id'], user_id2=msg['receiver_id'], status="pending",
                            created_at=datetime.now(timezone.utc))
                    db.add(add_friend)
                    db.commit()
                    db.refresh(add_friend)
                else:
                    if db_friend[0][1] == "friend":
                        raise Exception('You are already friends!')
            if msg['receiver_id'] not in connected_users:
                continue
            for user, user_ws in connected_users.items():
                if user == msg['receiver_id']:
                    json.dumps(msg)
                    await user_ws.send_json(msg)


    except Exception as e:
        # If a user disconnects, remove them from the dictionary
        print(e)
        if str(e) == 'User does not login or token is expired.':
            await connected_users[user_id].send_text("User does not login or token is expired.")
        del connected_users[user_id]
        await websocket.close()
