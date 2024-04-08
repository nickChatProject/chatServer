from pydantic import BaseModel
from typing import Any


class UserInfoBase(BaseModel):
    username: str
    comp_name: str
    dept_name: str


class UserNameBase(BaseModel):
    name: str


class UserBase(BaseModel):
    account: str
    password: str


class Users(UserBase):
    cid: int
    email: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    token: Any


class FriendIDBase(BaseModel):
    cid: int

