from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, String, ForeignKey
)

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    name = Column(String(100), nullable=False)

    subject = relationship("Subject", backref="topics")