from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.variant import Variant
from app.domain.interfaces import IVariantRepository


class VariantRepository(IVariantRepository):
    def __init__(self, session: Session):
        self.session = session

    def delete(self, variant_id: int) -> None:
        pass

    def update(self, variant_id: int, data: dict) -> Optional[Variant]:
        pass

    def list_by_subject(self, subject_id: Optional[int] = None) -> List[Variant]:
        pass

    def get_by_id(self, variant_id: int) -> Optional[Variant]:
        pass

    def create(self, variant: Variant) -> Variant:
        pass
