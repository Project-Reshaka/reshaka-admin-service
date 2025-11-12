from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.task_input import TaskInput
from app.domain.interfaces import ITaskInputRepository
from app.infrastructure.database.models import TaskInput as TaskInputModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class TaskInputRepository(ITaskInputRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: TaskInput) -> TaskInput:
        model = OrmEntityMapper.to_model(task, TaskInputModel)
        self.session.add(task)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, TaskInput)

    def get_by_id(self, task_id: int) -> Optional[TaskInput]:
        model = self.session.query(TaskInputModel).filter_by(id=task_id).first()
        return OrmEntityMapper.to_entity(model, TaskInput)

    def list(self) -> List[TaskInput]:
        models = self.session.query(TaskInputModel).order_by(TaskInputModel.id).all()
        return [OrmEntityMapper.to_entity(model, TaskInput) for model in models]

    def update(self, task_id: int, data: dict) -> Optional[TaskInput]:
        model = self.session.query(TaskInputModel).filter_by(id=task_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, TaskInput)

    def delete(self, task_id: int) -> None:
        self.session.query(TaskInputModel).filter_by(id=task_id).delete()
        self.session.commit()