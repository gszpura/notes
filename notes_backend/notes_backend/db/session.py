from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from notes_backend.core.config import settings


SQLALCHEMY_DATABASE_URI = "postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}".format(
    settings.DATABASE_USER,
    settings.DATABASE_PASSWORD,
    settings.DATABASE_HOST,
    settings.DATABASE_PORT,
    settings.DATABASE_NAME,
)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    future=True,
    echo=True,
)

async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
    future=True,
    autoflush=False,
)


async def get_db() -> AsyncIterator[AsyncSession]:
    async with async_session() as db:
        yield db
