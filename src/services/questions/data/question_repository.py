from typing import Optional
from sqlalchemy import select
from src.models import Question
from sqlalchemy.orm import selectinload
from ..question_schema import QuestionData
from sqlalchemy.ext.asyncio import AsyncSession


class QuestionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_question(self, data: QuestionData) -> Question:
        question = Question(**data.model_dump())
        self.db.add(question)
        await self.db.commit()
        await self.db.refresh(question)
        return question

    async def get_questions(self) -> list[Question]:
        statement = select(Question)
        result = await self.db.execute(statement=statement)
        return result.scalars().all()

    async def get_question_by_id(self, question_id: int) -> Optional[Question]:
        query = (
            select(Question)
            .options(selectinload(Question.answers))
            .where(Question.id == question_id)
        )
        result = await self.db.execute(query)
        return result.scalars().first()

    async def delete(self, question: Question) -> bool:
        await self.db.delete(question)
        await self.db.commit()
        return True
