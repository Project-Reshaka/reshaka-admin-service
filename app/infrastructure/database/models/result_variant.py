from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, DateTime, ForeignKey
)
from datetime import datetime


class ResultVariant(Base):
    __tablename__ = "results_variants"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    variant_id = Column(Integer, ForeignKey("variants.id", ondelete="CASCADE"))
    started_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime)
    total_questions = Column(Integer)
    correct_answers = Column(Integer)
    time_taken_sec = Column(Integer)

    user = relationship("User", backref="variant_results")
    variant = relationship("Variant", backref="results")