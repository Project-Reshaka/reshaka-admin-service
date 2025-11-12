from typing import Optional, List

from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.interfaces.user_interface import IUserRepository
from app.infrastructure.database.models import User as UserModel
from app.infrastructure.orm_entity_mapper import OrmEntityMapper


class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        model = OrmEntityMapper.to_model(user, UserModel)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, User)

    def get_by_id(self, user_id: int) -> Optional[User]:
        model = self.session.query(UserModel).filter_by(id=user_id).first()
        return OrmEntityMapper.to_entity(model, User)

    def get_by_username(self, username: str) -> Optional[User]:
        model = self.session.query(UserModel).order_by(username=username).first()
        return OrmEntityMapper.to_entity(model, User)

    def list(self) -> List[User]:
        models = self.session.query(UserModel).order_by(UserModel.id).all()
        return [OrmEntityMapper.to_entity(model, User) for model in models]

    def update(self, user_id: int, data: dict) -> Optional[User]:
        model = self.session.query(UserModel).filter_by(id=user_id).first()
        if not model:
            return None
        for key, value in data.items():
            setattr(model, key, value)

        self.session.commit()
        self.session.refresh(model)
        return OrmEntityMapper.to_entity(model, User)

    def delete(self, user_id: int) -> None:
        self.session.query(UserModel).filter_by(id=user_id).delete()
        self.session.commit()

