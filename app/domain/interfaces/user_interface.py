from abc import ABC, abstractmethod
from typing import Optional, List

from app.domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        ...

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        ...

    @abstractmethod
    def list(self) -> List[User]:
        ...

    @abstractmethod
    def update(self, user_id: int, data: dict) -> Optional[User]:
        ...

    @abstractmethod
    def delete(self, user_id: int) -> None:
        ...