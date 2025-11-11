from sqlalchemy.orm import relationship

from app.infrastructure.database.models.base import Base

from sqlalchemy import (
    Column, Integer, String, ForeignKey
)


class VariantTask(Base):
    __tablename__ = "variant_tasks"

    id = Column(Integer, primary_key=True)
    variant_id = Column(Integer, ForeignKey("variants.id", ondelete="CASCADE"))
    task_type = Column(String(20), nullable=False)
    task_id = Column(Integer, nullable=False)
    order_num = Column(Integer, default=0)

    variant = relationship("Variant", backref="tasks")