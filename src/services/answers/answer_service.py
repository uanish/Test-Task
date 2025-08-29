from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from .data.answer_repository import AnswerRepository
from .answer_schema import AnswerData, AnswerResponse
from src.services.questions.data.question_repository import QuestionRepository


class AnswerService:
    def __init__(self, db: AsyncSession):
        self.answer_repository = AnswerRepository(db)
        self.question_repository = QuestionRepository(db)

    async def create_answer(self, question_id: int, data: AnswerData) -> AnswerResponse:
        question = await self.question_repository.get_question_by_id(
            question_id=question_id
        )
        if question is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found",
            )
        result = await self.answer_repository.create_answer(
            question_id=question_id, data=data
        )
        return AnswerResponse(
            id=result.id,
            text=result.text,
            user_id=result.user_id,
            created_at=result.created_at,
            question_id=result.question_id,
        )

    async def get_answer_by_id(self, answer_id: int) -> AnswerResponse:
        answer = await self.answer_repository.get_answer_by_id(answer_id=answer_id)
        if answer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Answer not found",
            )
        return AnswerResponse(
            id=answer.id,
            text=answer.text,
            user_id=answer.user_id,
            created_at=answer.created_at,
            question_id=answer.question_id,
        )

    async def delete_answer(self, answer_id: int) -> None:
        answer = await self.answer_repository.get_answer_by_id(answer_id=answer_id)
        if answer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Answer not found",
            )
        await self.answer_repository.delete(answer)
        return
