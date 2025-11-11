from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResultVariantBase(BaseModel):
    user_id: int
    variant_id: int
    total_questions: Optional[int]
    correct_answers: Optional[int]
    time_taken_sec: Optional[int]


class ResultVariantRead(ResultVariantBase):
    id: int
    started_at: datetime
    finished_at: Optional[datetime]

    class Config:
        from_attributes = True