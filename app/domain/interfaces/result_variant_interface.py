from abc import abstractmethod, ABC
from typing import List, Optional

from app.domain.entities.result_variant import ResultVariant


class IResultVariantRepository(ABC):
    @abstractmethod
    def create(self, result: ResultVariant) -> ResultVariant:
        ...

    @abstractmethod
    def get_by_user(self, user_id: int) -> List[ResultVariant]:
        ...

    @abstractmethod
    def get_by_id(self, result_id: int) -> Optional[ResultVariant]:
        ...

    @abstractmethod
    def update(self, result_id: int, data: dict) -> Optional[ResultVariant]:
        ...