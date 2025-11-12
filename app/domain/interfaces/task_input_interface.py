from abc import ABC, abstractmethod
from typing import Optional, List

from app.domain.entities.task_input import TaskInput


class ITaskInputRepository(ABC):
    @abstractmethod
    def create(self, task: TaskInput) -> TaskInput:
        ...

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[TaskInput]:
        ...

    @abstractmethod
    def list(self) -> List[TaskInput]:
        ...

    @abstractmethod
    def update(self, task_id: int, data: dict) -> Optional[TaskInput]:
        ...

    @abstractmethod
    def delete(self, task_id: int) -> None:
        ...