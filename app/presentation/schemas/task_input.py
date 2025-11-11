from datetime import datetime
from typing import List, Any
from pydantic import BaseModel


class TaskInputBase(BaseModel):
    text: str
    correct_answers: List[Any]
    is_hard: bool = False


class TaskInputRead(TaskInputBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True