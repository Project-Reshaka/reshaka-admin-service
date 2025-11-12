from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.result_variant_task import ResultVariantTask


class IResultVariantTaskRepository(ABC):
    @abstractmethod
    def create(self, result: ResultVariantTask) -> ResultVariantTask:
        ...

    @abstractmethod
    def list_by_result(self, result_variant_id: int) -> List[ResultVariantTask]:
        ...

    @abstractmethod
    def delete(self, rv_task_id: int) -> None:
        ...