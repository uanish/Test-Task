import uuid
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, StringConstraints


class AnswerData(BaseModel):
    user_id: uuid.UUID
    text: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class AnswerResponse(AnswerData):
    id: int
    question_id: int
    created_at: datetime
