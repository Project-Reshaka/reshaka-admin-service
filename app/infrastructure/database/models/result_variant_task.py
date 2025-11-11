from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, String, ForeignKey, JSON, Boolean
)


class ResultVariantTask(Base):
    __tablename__ = "results_variant_tasks"

    id = Column(Integer, primary_key=True)
    result_variant_id = Column(Integer, ForeignKey("results_variants.id", ondelete="CASCADE"))
    task_type = Column(String(20), nullable=False)
    task_id = Column(Integer, nullable=False)
    selected_answer = Column(JSON)
    is_correct = Column(Boolean)
    time_taken_sec = Column(Integer)

    result_variant = relationship("ResultVariant", backref="detailed_tasks")