from pydantic import BaseModel


class TopicBase(BaseModel):
    name: str
    subject_id: int


class TopicRead(TopicBase):
    id: int

    class Config:
        from_attributes = True