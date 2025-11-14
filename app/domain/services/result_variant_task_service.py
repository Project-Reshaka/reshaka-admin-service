from typing import List
from app.domain.entities import ResultVariantTask
from app.domain.interfaces import IResultVariantTaskRepository, IResultVariantRepository


class ResultVariantTaskService:
    def __init__(self, result_variant_task_repo: IResultVariantTaskRepository, result_variant_repo: IResultVariantRepository):
        self.result_variant_task_repo = result_variant_task_repo
        self.result_variant_repo = result_variant_repo

    def create_result_variant_task(self, rv_task: ResultVariantTask) -> ResultVariantTask:
        parent = self.result_variant_repo.get_by_id(rv_task.result_variant_id)
        if not parent:
            raise ValueError(f"ResultVariant ID {rv_task.result_variant_id} not found")

        return self.result_variant_task_repo.create(rv_task)

    def list_by_result_variant(self, result_variant_id: int) -> List[ResultVariantTask]:
        return self.result_variant_task_repo.list_by_result(result_variant_id)

    def delete_result_variant_task(self, rv_task_id: int) -> None:
        self.result_variant_task_repo.delete(rv_task_id)
