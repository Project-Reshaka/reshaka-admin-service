from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.task_input import TaskInput
from app.domain.interfaces import ITaskInputRepository


class TaskInputRepository(ITaskInputRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: TaskInput) -> TaskInput:
        pass

    def get_by_id(self, task_id: int) -> Optional[TaskInput]:
        pass

    def list(self) -> List[TaskInput]:
        pass

    def update(self, task_id: int, data: dict) -> Optional[TaskInput]:
        pass

    def delete(self, task_id: int) -> None:
        pass