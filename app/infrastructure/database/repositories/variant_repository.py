from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.variant import Variant
from app.domain.interfaces import IVariantRepository
from app.infrastructure.database.models import Variant as VariantModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class VariantRepository(IVariantRepository):
    def __init__(self, session: Session):
        self.session = session

    def delete(self, variant_id: int) -> None:
        self.session.query(VariantModel).filter_by(id=variant_id).delete()
        self.session.commit()

    def update(self, variant_id: int, data: dict) -> Optional[Variant]:
        model = self.session.query(VariantModel).filter_by(id=variant_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, Variant)

    def list_by_subject(self, subject_id: Optional[int] = None) -> List[Variant]:
        models = self.session.query(VariantModel).filter_by(subject_id=subject_id).all()
        return [OrmEntityMapper.to_entity(model, Variant) for model in models]

    def get_by_id(self, variant_id: int) -> Optional[Variant]:
        model = self.session.query(VariantModel).filter_by(id=variant_id).first()
        return OrmEntityMapper.to_entity(model, Variant)

    def create(self, variant: Variant) -> Variant:
        model = OrmEntityMapper.to_model(variant, VariantModel)
        self.session.add(variant)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, Variant)
