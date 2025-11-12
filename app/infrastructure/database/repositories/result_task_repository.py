from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.result_task import ResultTask
from app.domain.interfaces import IResultTaskRepository


class ResultTaskRepository(IResultTaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, result: ResultTask) -> ResultTask:
        pass

    def get_by_user(self, user_id: int) -> List[ResultTask]:
        pass

    def delete(self, result_id: int) -> None:
        pass