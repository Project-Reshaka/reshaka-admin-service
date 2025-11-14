from typing import List, Optional
from app.domain.entities import ResultVariant
from app.domain.interfaces import IResultVariantRepository, IUserRepository


class ResultVariantService:
    def __init__(self, result_variant_repo: IResultVariantRepository, user_repo: IUserRepository):
        self.result_variant_repo = result_variant_repo
        self.user_repo = user_repo

    def create_result_variant(self, result_variant: ResultVariant) -> ResultVariant:
        return self.result_variant_repo.create(result_variant)

    def get_result_variant_by_user_id(self, user_id:int) -> List[ResultVariant]:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        return self.result_variant_repo.get_by_user(user_id)

    def get_result_variant_by_id(self, result_variant_id: int) -> Optional[ResultVariant]:
        result_variant = self.result_variant_repo.get_by_id(result_variant_id)
        if not result_variant:
            raise ValueError(f"Result variant with ID {result_variant_id} not found")
        return result_variant

    def update_result_variant(self, result_variant_id: int, data:dict) -> ResultVariant:
        updated = self.result_variant_repo.update(result_variant_id, data)
        if not updated:
            raise ValueError(f"Failed to update result variant with ID {result_variant_id}")
        return updated
