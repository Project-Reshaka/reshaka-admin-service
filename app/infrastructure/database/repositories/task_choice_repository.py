from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.task_choice import TaskChoice
from app.domain.interfaces import ITaskChoiceRepository
from app.infrastructure.database.models import TaskChoice as TaskChoiceModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class TaskChoiceRepository(ITaskChoiceRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: TaskChoice) -> TaskChoice:
        model = OrmEntityMapper.to_model(task, TaskChoiceModel)
        self.session.add(task)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, TaskChoice)

    def get_by_id(self, task_id: int) -> Optional[TaskChoice]:
        model = self.session.query(TaskChoiceModel).filter_by(id=task_id).first()
        return OrmEntityMapper.to_entity(model, TaskChoice)

    def list(self) -> List[TaskChoice]:
        models = self.session.query(TaskChoiceModel).order_by(TaskChoiceModel.id).all()
        return [OrmEntityMapper.to_entity(model, TaskChoice) for model in models]

    def update(self, task_id: int, data: dict) -> Optional[TaskChoice]:
        model = self.session.query(TaskChoiceModel).filter_by(id=task_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, TaskChoice)

    def delete(self, task_id: int) -> None:
        self.session.query(TaskChoiceModel).filter_by(id=task_id).delete()
        self.session.commit()
