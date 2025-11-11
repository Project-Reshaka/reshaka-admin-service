from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any


@dataclass
class ResultTask:
    id: Optional[int]
    user_id: int
    task_type: str
    task_id: int
    answered_at: Optional[datetime] = None
    selected_answer: Optional[Any] = None
    is_correct: Optional[bool] = None
    time_taken_sec: Optional[int] = None