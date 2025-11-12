from abc import ABC, abstractmethod
from typing import Optional, List

from app.domain.entities.task_manual import TaskManual


class ITaskManualRepository(ABC):
    @abstractmethod
    def create(self, task: TaskManual) -> TaskManual:
        ...

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[TaskManual]:
        ...

    @abstractmethod
    def list(self) -> List[TaskManual]:
        ...

    @abstractmethod
    def update(self, task_id: int, data: dict) -> Optional[TaskManual]:
        ...

    @abstractmethod
    def delete(self, task_id: int) -> None:
        ...