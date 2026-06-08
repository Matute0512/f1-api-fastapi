from collections.abc import AsyncGenerator

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from f1_api.infra.database import Base

# We use a static local file for tests so async threads can access it reliably.
# We will drop the tables after the test anyway to keep it clean.
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test_database.db"

test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
test_session_maker = async_sessionmaker(
    test_engine, class_=AsyncSession, expire_on_commit=False
)


@pytest.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Creates a fresh in-memory database for each test, yields the session,
    and then drops the tables to ensure complete isolation.
    """
    # Create tables before the test
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Give the session to the test
    async with test_session_maker() as session:
        yield session

    # Destroy tables after the test
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
