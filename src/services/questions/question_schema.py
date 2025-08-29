from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, StringConstraints
from src.services.answers.answer_schema import AnswerResponse


class QuestionData(BaseModel):
    text: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class QuestionResponse(QuestionData):
    id: int
    created_at: datetime


class QuestionDetail(QuestionResponse):
    answers: list[AnswerResponse]
