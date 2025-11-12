from typing import Optional, List

from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.interfaces.user_interface import IUserRepository
from app.infrastructure.database.models import User as UserModel


class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        model = self._to_orm_model(user)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(model)
        return self._to_entity(model)

    def get_by_id(self, user_id: int) -> Optional[User]:
        model = self.session.query(UserModel).filter_by(id=user_id).first()
        return self._to_entity(model)

    def get_by_username(self, username: str) -> Optional[User]:
        model = self.session.query(UserModel).order_by(username=username).first()
        return self._to_entity(model)

    def list(self) -> List[User]:
        models = self.session.query(UserModel).order_by(UserModel.id).all()
        # я хз ide кидает варнинг, который убрать можно через cast, но это будет заглушка, а это не надо
        return [self._to_entity(model) for model in models]

    def update(self, user_id: int, data: dict) -> Optional[User]:
        model = self.session.query(UserModel).filter_by(id=user_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return self._to_entity(model)

    def delete(self, user_id: int) -> None:
        self.session.query(UserModel).filter_by(id=user_id).delete()
        self.session.commit()

    @staticmethod
    def _to_orm_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            username=entity.username,
            password_hash=entity.password_hash,
            role=entity.role,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    @staticmethod
    def _to_entity(model: Optional[UserModel]) -> Optional[User]:
        if not model:
            return None
        return User(
            id=model.id,
            username=model.username,
            password_hash=model.password_hash,
            role=model.role,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )