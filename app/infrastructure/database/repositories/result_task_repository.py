from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.result_task import ResultTask
from app.domain.interfaces import IResultTaskRepository
from app.infrastructure.database.models import ResultTask as ResultTaskModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class ResultTaskRepository(IResultTaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, result: ResultTask) -> ResultTask:
        model = OrmEntityMapper.to_model(result, ResultTaskModel)
        self.session.add(result)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, ResultTask)

    def get_by_user(self, user_id: int) -> List[ResultTask]:
        models = self.session.query(ResultTaskModel).filter_by(user_id=user_id).all()
        return [OrmEntityMapper.to_entity(model, ResultTask) for model in models]

    def delete(self, result_id: int) -> None:
        self.session.query(ResultTaskModel).filter_by(id=result_id).delete()
        self.session.commit()

