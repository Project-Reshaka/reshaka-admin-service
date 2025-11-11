from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, DateTime, Text, JSON, Boolean
)
from datetime import datetime


class TaskInput(Base):
    __tablename__ = "tasks_input"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    correct_answers = Column(JSON, nullable=False)
    is_hard = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)