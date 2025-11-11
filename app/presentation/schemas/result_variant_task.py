from typing import Optional, Any
from pydantic import BaseModel


class ResultVariantTaskBase(BaseModel):
    result_variant_id: int
    task_type: str
    task_id: int
    selected_answer: Optional[Any]
    is_correct: Optional[bool]
    time_taken_sec: Optional[int]


class ResultVariantTaskRead(ResultVariantTaskBase):
    id: int

    class Config:
        from_attributes = True