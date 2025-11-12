from abc import abstractmethod, ABC
from typing import Optional, List

from app.domain.entities.subject import Subject


class ISubjectRepository(ABC):
    @abstractmethod
    def create(self, subject: Subject) -> Subject:
        ...

    @abstractmethod
    def get_by_id(self, subject_id: int) -> Optional[Subject]:
        ...

    @abstractmethod
    def list(self) -> List[Subject]:
        ...

    @abstractmethod
    def update(self, subject_id: int, data: dict) -> Optional[Subject]:
        ...

    @abstractmethod
    def delete(self, subject_id: int) -> None:
        ...