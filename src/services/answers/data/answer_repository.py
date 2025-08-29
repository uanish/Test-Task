from typing import Optional
from src.models import Answer
from sqlalchemy import select
from ..answer_schema import AnswerData
from sqlalchemy.ext.asyncio import AsyncSession


class AnswerRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_answer(self, question_id: int, data: AnswerData) -> Answer:
        answer = Answer(**data.model_dump(), question_id=question_id)
        self.db.add(answer)
        await self.db.commit()
        await self.db.refresh(answer)
        return answer

    async def get_answer_by_id(self, answer_id: int) -> Optional[Answer]:
        query = select(Answer).where(Answer.id == answer_id)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def delete(self, answer: Answer) -> bool:
        await self.db.delete(answer)
        await self.db.commit()
        return True
