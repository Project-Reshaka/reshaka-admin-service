from typing import List
from app.domain.entities import TaskManual
from app.domain.interfaces import ITaskManualRepository, ITopicRepository


class TaskManualService:
    def __init__(self, task_repo: ITaskManualRepository, topic_repo: ITopicRepository):
        self.task_repo = task_repo
        self.topic_repo = topic_repo

    def create_task(self, task: TaskManual) -> TaskManual:
        topic = self.topic_repo.get_by_id(task.id)
        if not topic:
            raise ValueError(f"Topic with ID {task.id} not found")

        return self.task_repo.create(task)

    def get_task(self, task_id: int) -> TaskManual:
        task = self.task_repo.get_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        return task

    def list_tasks(self) -> List[TaskManual]:
        return self.task_repo.list()

    def update_task(self, task_id: int, data: dict) -> TaskManual:
        updated = self.task_repo.update(task_id, data)
        if not updated:
            raise ValueError(f"Task with ID {task_id} not found")
        return updated

    def delete_task(self, task_id: int) -> None:
        task = self.task_repo.get_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")

        self.task_repo.delete(task_id)
