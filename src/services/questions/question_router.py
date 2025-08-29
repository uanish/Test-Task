from src.database import get_db
from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.questions.question_service import QuestionService
from .question_schema import QuestionData, QuestionResponse, QuestionDetail

router = APIRouter(prefix="/questions", tags=["questions"])


def get_question_crud(db: AsyncSession = Depends(get_db)) -> QuestionService:
    return QuestionService(db=db)


@router.post(
    path="/", status_code=status.HTTP_201_CREATED, response_model=QuestionResponse
)
async def create_question(
    request: QuestionData, service: QuestionService = Depends(get_question_crud)
):
    return await service.create_question(data=request)


@router.get(
    path="/", status_code=status.HTTP_200_OK, response_model=list[QuestionResponse]
)
async def get_questions(service: QuestionService = Depends(get_question_crud)):
    return await service.get_questions()


@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    response_model=QuestionDetail,
)
async def get_question(id: int, service: QuestionService = Depends(get_question_crud)):
    return await service.get_question_by_id(question_id=id)


@router.delete(
    path="/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None
)
async def delete_question(
    id: int, service: QuestionService = Depends(get_question_crud)
):
    return await service.delete_question(question_id=id)
