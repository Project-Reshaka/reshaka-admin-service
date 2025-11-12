from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.result_variant import ResultVariant
from app.domain.interfaces import IResultVariantRepository


class ResultVariantRepository(IResultVariantRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, result: ResultVariant) -> ResultVariant:
        pass

    def get_by_user(self, user_id: int) -> List[ResultVariant]:
        pass

    def get_by_id(self, result_id: int) -> Optional[ResultVariant]:
        pass

    def update(self, result_id: int, data: dict) -> Optional[ResultVariant]:
        pass