from typing import List

from sqlalchemy.orm import Session

from app.domain.entities.result_variant_task import ResultVariantTask
from app.domain.interfaces import IResultVariantTaskRepository
from app.infrastructure.database.models import ResultVariantTask as ResultVariantTaskModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class ResultVariantTaskRepository(IResultVariantTaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, result: ResultVariantTask) -> ResultVariantTask:
        model = OrmEntityMapper.to_model(result, ResultVariantTaskModel)
        self.session.add(result)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, ResultVariantTask)

    def list_by_result(self, result_variant_id: int) -> List[ResultVariantTask]:
        models = self.session.query(ResultVariantTaskModel).filter_by(result_variant_id = result_variant_id).all()
        return [OrmEntityMapper.to_entity(model, ResultVariantTask) for model in models]

    def delete(self, rv_task_id: int) -> None:
        self.session.query(ResultVariantTaskModel).filter_by(id=rv_task_id).delete()
        self.session.commit()
