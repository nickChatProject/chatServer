from pydantic import BaseModel
from typing import Any


class UserOrgBase(BaseModel):
    comp_name: str
    dept_name: str


class UserEmailBase(BaseModel):
    email: str


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

