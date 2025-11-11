from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Any


@dataclass
class TaskInput:
    id: Optional[int]
    text: str
    correct_answers: List[Any]
    is_hard: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None