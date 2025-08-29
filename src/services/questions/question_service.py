from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from .data.question_repository import QuestionRepository
from src.services.answers.answer_schema import AnswerResponse
from .question_schema import QuestionData, QuestionResponse, QuestionDetail


class QuestionService:
    def __init__(self, db: AsyncSession):
        self.question_repository = QuestionRepository(db)

    async def create_question(self, data: QuestionData) -> QuestionResponse:
        result = await self.question_repository.create_question(data=data)
        return QuestionResponse(
            id=result.id, text=result.text, created_at=result.created_at
        )

    async def get_questions(self) -> list[QuestionResponse]:
        questions = await self.question_repository.get_questions()
        return [
            QuestionResponse(
                id=question.id, text=question.text, created_at=question.created_at
            )
            for question in questions
        ]

    async def get_question_by_id(self, question_id: int) -> QuestionDetail:
        question = await self.question_repository.get_question_by_id(
            question_id=question_id
        )
        if question is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found",
            )
        return QuestionDetail(
            id=question.id,
            text=question.text,
            created_at=question.created_at,
            answers=[
                AnswerResponse(
                    id=answer.id,
                    user_id=answer.user_id,
                    question_id=answer.question_id,
                    text=answer.text,
                    created_at=answer.created_at,
                )
                for answer in question.answers
            ],
        )

    async def delete_question(self, question_id: int) -> None:
        question = await self.question_repository.get_question_by_id(
            question_id=question_id
        )
        if question is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found",
            )
        await self.question_repository.delete(question=question)
        return
