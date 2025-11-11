from datetime import datetime

from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, String, ForeignKey, Text, Boolean, DateTime
)

class Variant(Base):
    __tablename__ = "variants"

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    author_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    name = Column(String(100), nullable=False)
    description = Column(Text)
    is_timed = Column(Boolean, default=False)
    time_limit_sec = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    subject = relationship("Subject", backref="variants")
    author = relationship("User", backref="created_variants")