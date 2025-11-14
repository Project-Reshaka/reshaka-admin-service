from typing import List
from app.domain.entities import VariantTask
from app.domain.interfaces import IVariantTaskRepository, IVariantRepository


class VariantTaskService:
    def __init__(self, variant_task_repo: IVariantTaskRepository, variant_repo: IVariantRepository):
        self.variant_task_repo = variant_task_repo
        self.variant_repo = variant_repo

    def add_task(self, vt: VariantTask) -> VariantTask:
        variant = self.variant_repo.get_by_id(vt.variant_id)
        if not variant:
            raise ValueError(f"Variant with ID {vt.variant_id} not found")

        return self.variant_task_repo.add_task(vt)

    def list_by_variant(self, variant_id: int) -> List[VariantTask]:
        return self.variant_task_repo.list_by_variant(variant_id)

    def delete(self, vt_id: int) -> None:
        self.variant_task_repo.delete(vt_id)
