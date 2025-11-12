from abc import abstractmethod, ABC
from typing import List

from app.domain.entities.variant_task import VariantTask


class IVariantTaskRepository(ABC):
    @abstractmethod
    def add_task(self, vt: VariantTask) -> VariantTask:
        ...

    @abstractmethod
    def list_by_variant(self, variant_id: int) -> List[VariantTask]:
        ...

    @abstractmethod
    def delete(self, vt_id: int) -> None:
        ...
