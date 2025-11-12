from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.topic import Topic
from app.domain.interfaces import ITopicRepository
from app.infrastructure.database.models import Topic as TopicModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class TopicRepository(ITopicRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, topic: Topic) -> Topic:
        model = OrmEntityMapper.to_model(topic, TopicModel)
        self.session.add(topic)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, Topic)

    def get_by_id(self, topic_id: int) -> Optional[Topic]:
        model = self.session.query(TopicModel).filter_by(id=topic_id).first()
        return OrmEntityMapper.to_entity(model, Topic)

    def list_by_subject(self, subject_id) -> List[Topic]:
        models = self.session.query(TopicModel).filter_by(subject_id=subject_id).all()
        return [OrmEntityMapper.to_entity(model, Topic) for model in models]

    def update(self, topic_id: int, data: dict) -> Optional[Topic]:
        model = self.session.query(TopicModel).filter_by(id=topic_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, Topic)

    def delete(self, topic_id) -> None:
        self.session.query(TopicModel).filter_by(id=topic_id).delete()
        self.session.commit()
