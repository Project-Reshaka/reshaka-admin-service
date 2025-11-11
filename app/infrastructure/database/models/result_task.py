from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey, JSON, Boolean
)
from datetime import datetime


class ResultTask(Base):
    __tablename__ = "results_tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    task_type = Column(String(20), nullable=False)
    task_id = Column(Integer, nullable=False)
    answered_at = Column(DateTime, default=datetime.utcnow)
    selected_answer = Column(JSON)
    is_correct = Column(Boolean)
    time_taken_sec = Column(Integer)

    user = relationship("User", backref="task_results")