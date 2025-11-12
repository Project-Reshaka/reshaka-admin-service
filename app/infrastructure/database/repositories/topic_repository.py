from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.topic import Topic
from app.domain.interfaces import ITopicRepository


class TopicRepository(ITopicRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, topic: Topic) -> Topic:
        pass

    def get_by_id(self, topic_id: int) -> Optional[Topic]:
        pass

    def list_by_subject(self, subject_id) -> List[Topic]:
        pass

    def update(self, topic_id: int, data: dict) -> Optional[Topic]:
        pass

    def delete(self, topic_id) -> None:
        pass
