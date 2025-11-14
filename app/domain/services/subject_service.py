from typing import List
from app.domain.entities import Subject
from app.domain.interfaces import ISubjectRepository


class SubjectService:
    def __init__(self, subject_repo: ISubjectRepository):
        self.subject_repo = subject_repo

    def create_subject(self, subject: Subject) -> Subject:
        return self.subject_repo.create(subject)

    def get_subject(self, subject_id: int) -> Subject:
        subject = self.subject_repo.get_by_id(subject_id)
        if not subject:
            raise ValueError(f"Subject with ID {subject_id} not found")
        return subject

    def list_subjects(self) -> List[Subject]:
        return self.subject_repo.list()

    def update_subject(self, subject_id: int, data: dict) -> Subject:
        updated = self.subject_repo.update(subject_id, data)
        if not updated:
            raise ValueError(f"Subject with ID {subject_id} not found")
        return updated

    def delete_subject(self, subject_id: int) -> None:
        subject = self.subject_repo.get_by_id(subject_id)
        if not subject:
            raise ValueError(f"Subject with ID {subject_id} not found")
        self.subject_repo.delete(subject_id)
