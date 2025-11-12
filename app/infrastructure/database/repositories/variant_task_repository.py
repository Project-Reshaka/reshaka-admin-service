from typing import List

from sqlalchemy.orm import Session

from app.domain.entities.variant_task import VariantTask
from app.domain.interfaces import IVariantTaskRepository
from app.infrastructure.database.models import VariantTask as VariantTaskModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class VariantTaskRepository(IVariantTaskRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_task(self, vt: VariantTask) -> VariantTask:
        model = OrmEntityMapper.to_model(vt, VariantTaskModel)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, VariantTask)

    def list_by_variant(self, variant_id: int) -> List[VariantTask]:
        models = (
            self.session.query(VariantTaskModel)
            .filter_by(variant_id=variant_id)
            .all()
        )
        return [OrmEntityMapper.to_entity(model, VariantTask) for model in models]

    def delete(self, vt_id: int) -> None:
        self.session.query(VariantTaskModel).filter_by(id=vt_id).delete()
        self.session.commit()
