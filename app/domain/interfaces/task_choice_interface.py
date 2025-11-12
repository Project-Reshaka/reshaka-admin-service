from abc import abstractmethod, ABC
from typing import Optional, List

from app.domain.entities.task_choice import TaskChoice


class ITaskChoiceRepository(ABC):
    @abstractmethod
    def create(self, task: TaskChoice) -> TaskChoice:
        ...

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[TaskChoice]:
        ...

    @abstractmethod
    def list(self) -> List[TaskChoice]:
        ...

    @abstractmethod
    def update(self, task_id: int, data: dict) -> Optional[TaskChoice]:
        ...

    @abstractmethod
    def delete(self, task_id: int) -> None:
        ...