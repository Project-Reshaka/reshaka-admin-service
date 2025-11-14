from typing import List
from app.domain.entities import ResultTask
from app.domain.interfaces import IResultTaskRepository, IUserRepository


class ResultTaskService:
    def __init__(self, result_task_repo: IResultTaskRepository, user_repo: IUserRepository):
        self.user_repo = user_repo
        self.result_task_repo = result_task_repo
        
    def create_result_task(self, result: ResultTask) -> ResultTask:
        user = self.user_repo.get_by_id(result.user_id)
        if not user:
            raise ValueError(f"User with ID {result.user_id} not found")

        return self.result_task_repo.create(result)
    
    def get_result_task_by_user(self, user_id: int) -> List[ResultTask]:
        user = self.user_repo.get_by_id(user_id=user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        return self.result_task_repo.get_by_user(user_id)

    def delete_result_task(self, result_id) -> None:
       return self.result_task_repo.delete(result_id)