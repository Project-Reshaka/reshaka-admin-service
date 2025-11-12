from typing import List

from sqlalchemy.orm import Session

from app.domain.entities.variant_task import VariantTask
from app.domain.interfaces import IVariantTaskRepository


class VariantTaskRepository(IVariantTaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_task(self, vt: VariantTask) -> VariantTask:
        pass

    def list_by_variant(self, variant_id: int) -> List[VariantTask]:
        pass

    def delete(self, vt_id: int) -> None:
        pass
