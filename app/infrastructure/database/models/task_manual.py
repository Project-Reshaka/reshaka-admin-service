from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, DateTime, Text, Boolean
)
from datetime import datetime

class TaskManual(Base):
    __tablename__ = "tasks_manual"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    is_hard = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)