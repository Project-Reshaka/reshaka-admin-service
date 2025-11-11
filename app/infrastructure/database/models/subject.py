from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, String
)


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
