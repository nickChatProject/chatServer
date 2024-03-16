from sqlalchemy import Column, Integer, String, DateTime

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
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
