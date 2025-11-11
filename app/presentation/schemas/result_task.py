from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel


class ResultTaskBase(BaseModel):
    user_id: int
    task_type: str
    task_id: int
    selected_answer: Optional[Any]
    is_correct: Optional[bool]
    time_taken_sec: Optional[int]


class ResultTaskRead(ResultTaskBase):
    id: int
    answered_at: datetime

    class Config:
        from_attributes = True