from abc import abstractmethod, ABC
from typing import Optional, List

from app.domain.entities.topic import Topic


class ITopicInterface(ABC):
    @abstractmethod
    def create(self, topic: Topic) -> Topic:
        ...

    @abstractmethod
    def get_by_id(self, topic_id:int) -> Optional[Topic]:
        ...

    @abstractmethod
    def list_by_subject(self, subject_id) -> List[Topic]:
        ...

    @abstractmethod
    def update(self, topic_id: int, data: dict) -> Optional[Topic]:
        ...

    @abstractmethod
    def delete(self, topic_id) -> None:
        ...