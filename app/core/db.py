from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
    AsyncEngine,
)


async def start_async_engine(database_url: str) -> AsyncEngine:
    return create_async_engine(database_url)


async def make_async_session(engine: AsyncEngine) -> AsyncSession:
    if engine is None:
        engine = start_async_engine()
    return async_sessionmaker(engine, expire_on_commit=False)
