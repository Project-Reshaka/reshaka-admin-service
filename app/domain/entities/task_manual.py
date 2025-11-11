from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TaskManual:
    id: Optional[int]
    text: str
    is_hard: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None