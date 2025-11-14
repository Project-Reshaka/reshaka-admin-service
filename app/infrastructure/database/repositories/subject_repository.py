from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.subject import Subject
from app.domain.interfaces import ISubjectRepository
from app.infrastructure.database.models import Subject as SubjectModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class SubjectRepository(ISubjectRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, subject: Subject) -> Subject:
        model = OrmEntityMapper.to_model(subject, SubjectModel)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, SubjectModel)

    def get_by_id(self, subject_id: int) -> Optional[Subject]:
        model = self.session.query(SubjectModel).filter_by(id=subject_id).first()
        return OrmEntityMapper.to_entity(model, Subject)

    def list(self) -> List[Subject]:
        models = self.session.query(SubjectModel).order_by(SubjectModel.id).all()
        return [OrmEntityMapper.to_entity(model, Subject) for model in models]

    def update(self, subject_id: int, data: dict) -> Optional[Subject]:
        model = self.session.query(SubjectModel).filter_by(id=subject_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, Subject)

    def delete(self, subject_id: int) -> None:
        self.session.query(SubjectModel).filter_by(id=subject_id).delete()
        self.session.commit()