from datetime import datetime
from pydantic import BaseModel


class TaskManualBase(BaseModel):
    text: str
    is_hard: bool = False


class TaskManualRead(TaskManualBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True