from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.result_task import ResultTask


class IResultTaskRepository(ABC):
    @abstractmethod
    def create(self, result: ResultTask) -> ResultTask:
        ...

    @abstractmethod
    def get_by_user(self, user_id: int) -> List[ResultTask]:
        ...

    @abstractmethod
    def delete(self, result_id: int) -> None:
        ...