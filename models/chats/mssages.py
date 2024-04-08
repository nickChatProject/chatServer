from sqlalchemy import Column, Integer, String, DateTime

from models.db_connection.database import Base


class Msg(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    sender_id = Column(Integer)
    receiver_id = Column(Integer)
    content = Column(String)
    created_at = Column(DateTime)
