from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.task_choice import TaskChoice
from app.domain.interfaces import ITaskChoiceRepository


class TaskChoiceRepository(ITaskChoiceRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: TaskChoice) -> TaskChoice:
        pass

    def get_by_id(self, task_id: int) -> Optional[TaskChoice]:
        pass

    def list(self) -> List[TaskChoice]:
        pass

    def update(self, task_id: int, data: dict) -> Optional[TaskChoice]:
        pass

    def delete(self, task_id: int) -> None:
        pass
