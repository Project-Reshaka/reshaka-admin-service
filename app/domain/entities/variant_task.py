from dataclasses import dataclass
from typing import Optional, List, Any


@dataclass
class VariantTask:
    id: Optional[int]
    variant_id: int
    task_type: str
    task_id: int
    order_num: int = 0