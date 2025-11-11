from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Variant:
    id: Optional[int]
    subject_id: int
    author_id: Optional[int]
    name: str
    description: Optional[str]
    is_timed: bool = False
    time_limit_sec: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None