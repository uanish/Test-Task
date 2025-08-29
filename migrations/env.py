from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from src.database import Base

from src.models import Question, Answer
from alembic import context
from src.config import get_settings
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


DATABASE_URL = get_settings().db_uri


def run_migrations_offline():
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
