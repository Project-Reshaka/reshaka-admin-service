from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class ResultVariantTask:
    id: Optional[int]
    result_variant_id: int
    task_type: str
    task_id: int
    selected_answer: Optional[Any]
    is_correct: Optional[bool]
    time_taken_sec: Optional[int]