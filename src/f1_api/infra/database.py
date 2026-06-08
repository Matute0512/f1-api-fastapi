from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from f1_api.core.config import settings

# 1. Create the Async Engine (The actual connection to the database)
# check_same_thread is only needed for SQLite to avoid issues with Asyncio
engine = create_async_engine(
    settings.database_url,
    # Set to True to print all SQL queries to the terminal (useful for debugging)
    echo=False,
    connect_args=(
        {"check_same_thread": False} if "sqlite" in settings.database_url else {}
    ),
)

# 2. Create the Session Factory (Creates individual conversations with the DB)
async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
)

# 3. Base class for all our SQLAlchemy Models


class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy declarative models.
    All our future database tables will inherit from this.
    """

    pass


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency that provides a database session per request.
    It ensures the session is properly closed after the request finishes.
    """
    async with async_session_maker() as session:
        yield session
