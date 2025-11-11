from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, String, DateTime, JSON, Boolean, Text
)
from datetime import datetime


class TaskChoice(Base):
    __tablename__ = "tasks_choice"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    type = Column(String(10), nullable=False)
    options = Column(JSON, nullable=False)
    correct_answer = Column(JSON, nullable=False)
    is_hard = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)