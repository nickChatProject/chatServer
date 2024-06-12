import traceback

from fastapi import APIRouter, Request, Depends
from sqlalchemy import and_
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.models.chats.mssages import Msg
from app.models.chats.schemas import ChatReceiverBase
from app.models.db_connection.database import get_db

router = APIRouter()


# @router.websocket("/ws/{user_id}/")
# async def websocket_endpoint(user_id: str, websocket: WebSocket):
#     await websocket.accept()
#
#     # Store the WebSocket connection in the dictionary
#     connected_users[user_id] = websocket
#
#     try:
#         while True:
#             data = await websocket.receive_text()
#             # Send the received data to the other user
#             for user, user_ws in connected_users.items():
#                 if user != user_id:
#                     await user_ws.send_text(data)
#     except:
#         # If a user disconnects, remove them from the dictionary
#         del connected_users[user_id]

@router.post('/chat_history/')
def chat_history(request: Request, receiver: ChatReceiverBase, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        messages = (db.query(Msg.id, Msg.type, Msg.sender_id, Msg.receiver_id, Msg.content, Msg.created_at)
                    .filter(and_(Msg.sender_id == cid, Msg.receiver_id == receiver.receiver_id) |
                            and_(Msg.sender_id == receiver.receiver_id, Msg.receiver_id == cid))
                    .order_by(Msg.created_at).all())
        if len(messages) == 0:
            return JSONResponse([])

        messages_list = []
        for msg in messages:
            msg_dict = {
                'id': msg[0],
                'type': msg[1],
                'sender_id': msg[2],
                'receiver_id': msg[3],
                'content': msg[4],
                'created_at': msg[5].strftime("%m/%d/%Y, %H:%M")
            }
            messages_list.append(msg_dict)

        return JSONResponse(messages_list)

    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)
