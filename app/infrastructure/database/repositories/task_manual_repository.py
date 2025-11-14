from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.task_manual import TaskManual
from app.domain.interfaces import ITaskManualRepository
from app.infrastructure.database.models import TaskManual as TaskManualModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class TaskManualRepository(ITaskManualRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: TaskManual) -> TaskManual:
        model = OrmEntityMapper.to_model(task, TaskManualModel)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, TaskManual)

    def get_by_id(self, task_id: int) -> Optional[TaskManual]:
        model = self.session.query(TaskManualModel).filter_by(id=task_id).first()
        return OrmEntityMapper.to_entity(model, TaskManual)

    def list(self) -> List[TaskManual]:
        models = self.session.query(TaskManualModel).order_by(TaskManualModel.id).all()
        return [OrmEntityMapper.to_entity(model, TaskManual) for model in models]

    def update(self, task_id: int, data: dict) -> Optional[TaskManual]:
        model = self.session.query(TaskManualModel).filter_by(id=task_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, TaskManual)

    def delete(self, task_id: int) -> None:
        self.session.query(TaskManualModel).filter_by(id=task_id).delete()
        self.session.commit()