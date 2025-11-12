from typing import List, Optional
from app.domain.entities.user import User
from app.domain.interfaces import IUserRepository


class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def create_user(self, user: User) -> User:
        existing = self.user_repo.get_by_username(user.username)
        if existing:
            raise ValueError(f"User '{user.username}' already exists")
        return self.user_repo.create(user)

    def get_user(self, user_id: int) -> Optional[User]:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        return user

    def list_users(self) -> List[User]:
        return self.user_repo.list()

    def update_user(self, user_id: int, data: dict) -> User:
        if "username" in data:
            existing = self.user_repo.get_by_username(data["username"])
            if existing and existing.id != user_id:
                raise ValueError(f"Username '{data['username']}' is already taken")

        updated = self.user_repo.update(user_id, data)
        if not updated:
            raise ValueError(f"Failed to update user with ID {user_id}")
        return updated

    def delete_user(self, user_id: int) -> None:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")

        self.user_repo.delete(user_id)
