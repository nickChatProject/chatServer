from pydantic import BaseModel


class ChatReceiverBase(BaseModel):
    receiver_id: int
