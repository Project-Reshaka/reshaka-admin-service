from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class VariantBase(BaseModel):
    subject_id: int
    author_id: Optional[int]
    name: str
    description: Optional[str]
    is_timed: bool = False
    time_limit_sec: Optional[int]


class VariantRead(VariantBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True