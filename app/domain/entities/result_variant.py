from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ResultVariant:
    id: Optional[int]
    user_id: int
    variant_id: int
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    total_questions: Optional[int] = None
    correct_answers: Optional[int] = None
    time_taken_sec: Optional[int] = None
