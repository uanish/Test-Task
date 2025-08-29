from src.database import get_db
from .answer_service import AnswerService
from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .answer_schema import AnswerData, AnswerResponse

router = APIRouter(prefix="/answers", tags=["answers"])


def get_answer_crud(db: AsyncSession = Depends(get_db)) -> AnswerService:
    return AnswerService(db=db)


@router.post(
    path="/questions/{id}/answer",
    status_code=status.HTTP_201_CREATED,
    response_model=AnswerResponse,
)
async def create_answer(
    id: int, request: AnswerData, service: AnswerService = Depends(get_answer_crud)
):
    return await service.create_answer(question_id=id, data=request)


@router.get(path="/{id}", status_code=status.HTTP_200_OK, response_model=AnswerResponse)
async def get_answer(id: int, service: AnswerService = Depends(get_answer_crud)):
    return await service.get_answer_by_id(answer_id=id)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_answer(id: int, service: AnswerService = Depends(get_answer_crud)):
    return await service.delete_answer(answer_id=id)
