from typing import List

from sqlalchemy.orm import Session

from app.domain.entities.result_variant_task import ResultVariantTask
from app.domain.interfaces import IResultVariantTaskRepository


class ResultVariantTaskRepository(IResultVariantTaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, result: ResultVariantTask) -> ResultVariantTask:
        pass

    def list_by_result(self, result_variant_id: int) -> List[ResultVariantTask]:
        pass

    def delete(self, rv_task_id: int) -> None:
        pass