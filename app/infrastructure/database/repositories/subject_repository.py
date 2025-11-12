from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.subject import Subject
from app.domain.interfaces import ISubjectRepository


class SubjectRepository(ISubjectRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, subject: Subject) -> Subject:
        pass

    def get_by_id(self, subject_id: int) -> Optional[Subject]:
        pass

    def list(self) -> List[Subject]:
        pass

    def update(self, subject_id: int, data: dict) -> Optional[Subject]:
        pass

    def delete(self, subject_id: int) -> None:
        pass