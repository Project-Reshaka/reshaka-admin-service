from pydantic import BaseModel


class VariantTaskBase(BaseModel):
    variant_id: int
    task_type: str
    task_id: int
    order_num: int = 0


class VariantTaskRead(VariantTaskBase):
    id: int

    class Config:
        from_attributes = True
