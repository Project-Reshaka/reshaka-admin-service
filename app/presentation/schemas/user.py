from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    role: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True