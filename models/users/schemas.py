from pydantic import BaseModel


class UserBase(BaseModel):
    account: str
    password: str


class Users(UserBase):
    cid: int
    email: str

    class Config:
        from_attributes = True
