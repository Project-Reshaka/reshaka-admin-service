from typing import List
from app.domain.entities import Variant
from app.domain.interfaces import IVariantRepository, ISubjectRepository


class VariantService:
    def __init__(self, variant_repo: IVariantRepository, subject_repo: ISubjectRepository):
        self.variant_repo = variant_repo
        self.subject_repo = subject_repo

    def create_variant(self, variant: Variant) -> Variant:
        subject = self.subject_repo.get_by_id(variant.subject_id)
        if not subject:
            raise ValueError(f"Subject with ID {variant.subject_id} not found")

        return self.variant_repo.create(variant)

    def get_variant(self, variant_id: int) -> Variant:
        variant = self.variant_repo.get_by_id(variant_id)
        if not variant:
            raise ValueError(f"Variant with ID {variant_id} not found")
        return variant

    def list_by_subject(self, subject_id: int) -> List[Variant]:
        return self.variant_repo.list_by_subject(subject_id)

    def update_variant(self, variant_id: int, data: dict) -> Variant:
        updated = self.variant_repo.update(variant_id, data)
        if not updated:
            raise ValueError(f"Variant with ID {variant_id} not found")
        return updated

    def delete_variant(self, variant_id: int) -> None:
        variant = self.variant_repo.get_by_id(variant_id)
        if not variant:
            raise ValueError(f"Variant with ID {variant_id} not found")

        self.variant_repo.delete(variant_id)
