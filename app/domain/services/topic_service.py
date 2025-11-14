from typing import List
from app.domain.entities import Topic
from app.domain.interfaces import ITopicRepository, ISubjectRepository


class TopicService:
    def __init__(self, topic_repo: ITopicRepository, subject_repo: ISubjectRepository):
        self.topic_repo = topic_repo
        self.subject_repo = subject_repo

    def create_topic(self, topic: Topic) -> Topic:
        subject = self.subject_repo.get_by_id(topic.subject_id)
        if not subject:
            raise ValueError(f"Subject with ID {topic.subject_id} not found")

        return self.topic_repo.create(topic)

    def get_topic(self, topic_id: int) -> Topic:
        topic = self.topic_repo.get_by_id(topic_id)
        if not topic:
            raise ValueError(f"Topic with ID {topic_id} not found")
        return topic

    def list_by_subject(self, subject_id: int) -> List[Topic]:
        return self.topic_repo.list_by_subject(subject_id)

    def update_topic(self, topic_id: int, data: dict) -> Topic:
        updated = self.topic_repo.update(topic_id, data)
        if not updated:
            raise ValueError(f"Topic with ID {topic_id} not found")
        return updated

    def delete_topic(self, topic_id: int) -> None:
        topic = self.topic_repo.get_by_id(topic_id)
        if not topic:
            raise ValueError(f"Topic with ID {topic_id} not found")
        self.topic_repo.delete(topic_id)
