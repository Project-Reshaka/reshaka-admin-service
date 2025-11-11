from dataclasses import dataclass
from typing import Optional


@dataclass
class Topic:
    id: Optional[int]
    subject_id: int
    name: str
