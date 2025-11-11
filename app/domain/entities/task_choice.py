from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class TaskChoice:
    id: Optional[int]
    text: str
    type: str
    options: List[dict]
    correct_answer: List[int]
    is_hard: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None