from abc import ABC, abstractmethod
from typing import Optional, List

from app.domain.entities.variant import Variant


class IVariantRepository(ABC):
    @abstractmethod
    def create(self, variant: Variant) -> Variant:
        ...

    @abstractmethod
    def get_by_id(self, variant_id: int) -> Optional[Variant]:
        ...

    @abstractmethod
    def list_by_subject(self, subject_id: Optional[int] = None) -> List[Variant]:
        ...

    @abstractmethod
    def update(self, variant_id: int, data: dict) -> Optional[Variant]:
        ...

    @abstractmethod
    def delete(self, variant_id: int) -> None:
        ...