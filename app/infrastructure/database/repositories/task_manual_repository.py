from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.task_manual import TaskManual
from app.domain.interfaces import ITaskManualRepository


class TaskManualRepository(ITaskManualRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: TaskManual) -> TaskManual:
        pass

    def get_by_id(self, task_id: int) -> Optional[TaskManual]:
        pass

    def list(self) -> List[TaskManual]:
        pass

    def update(self, task_id: int, data: dict) -> Optional[TaskManual]:
        pass

    def delete(self, task_id: int) -> None:
        pass