import datetime
from pydantic import BaseModel, field_validator


class Question(BaseModel):
    id: int
    subject: str
    # Default값이 필요하면 subject: str | None = None
    content: str
    create_date: datetime.datetime


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator("subject", "content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v
