from datetime import datetime
from typing import List
from pydantic import BaseModel

class TaskChoiceBase(BaseModel):
    text: str
    type: str
    options: List[dict]
    correct_answer: List[int]
    is_hard: bool = False


class TaskChoiceRead(TaskChoiceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True