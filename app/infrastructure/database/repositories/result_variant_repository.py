from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.result_variant import ResultVariant
from app.domain.interfaces import IResultVariantRepository
from app.infrastructure.database.models import ResultVariant as ResultVariantModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class ResultVariantRepository(IResultVariantRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, result: ResultVariant) -> ResultVariant:
        model = OrmEntityMapper.to_model(result, ResultVariantModel)
        self.session.add(result)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, ResultVariant)

    def get_by_user(self, user_id: int) -> List[ResultVariant]:
        models = self.session.query(ResultVariantModel).filter_by(user_id=user_id).all()
        return [OrmEntityMapper.to_entity(model, ResultVariant) for model in models]

    def get_by_id(self, result_id: int) -> Optional[ResultVariant]:
        model = self.session.query(ResultVariantModel).filter_by(id=result_id).first()
        return OrmEntityMapper.to_entity(model, ResultVariant)

    def update(self, result_id: int, data: dict) -> Optional[ResultVariant]:
        model = self.session.query(ResultVariantModel).filter_by(id=result_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, ResultVariant)
