from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from models.db_connection.database import Base


class Users(Base):
    __tablename__ = "user_client"

    cid = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    account = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    company_id = Column(Integer, default=None)
    dept_id = Column(Integer, default=None)
    picture = Column(String, default=None)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Friends(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id1 = Column(Integer, nullable=False)
    user_id2 = Column(Integer, nullable=False)
    status = Column(String)
    created_at = Column(DateTime)
