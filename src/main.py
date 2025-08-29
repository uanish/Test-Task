from fastapi import FastAPI
from src.config import get_settings
from src.database import Base, engine
from contextlib import asynccontextmanager

from .services.questions import question_router
from .services.answers import answer_router


def init_router(_app: FastAPI) -> None:
    api_prefix = get_settings().api_prefix
    _app.include_router(answer_router.router, prefix=api_prefix)
    _app.include_router(question_router.router, prefix=api_prefix)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
init_router(app)
