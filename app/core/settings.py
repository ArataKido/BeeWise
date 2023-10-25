from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import Optional
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
    AsyncEngine,
)
import os
from app.core.types import DbHostname, DbName, DbPassword, DbPort, DbUser


class DatabaseSettings(BaseModel):
    db_hostname: DbHostname
    db_port: DbPort
    db_name: DbName
    db_password: DbPassword
    db_user: DbUser


class Database(BaseSettings):
    sub_model: DatabaseSettings

    @staticmethod
    def dsn(params) -> str:
        return f"postgresql+asyncpg://{params.db_user}:{params.db_password}@{params.db_hostname}:{params.db_port}/{params.db_name}"

    async def async_engine(self, database_url: str) -> AsyncEngine:
        return create_async_engine(database_url)

    async def async_session(self, engine: Optional[AsyncEngine] = None) -> AsyncSession:
        if engine is None:
            engine = await self.async_engine(self.dsn(self.sub_model))

        return async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncSession:
    db_settings = DatabaseSettings(
        db_name=os.environ["DB_NAME"],
        db_user=os.environ["DB_USER"],
        db_password=os.environ["DB_PASSWORD"],
        db_hostname=os.environ["DB_HOSTNAME"],
        db_port=os.environ["DB_PORT"],
    )
    db = Database(sub_model=db_settings)

    Session = await db.async_session()

    async with Session() as session:
        try:
            yield session
        except Exception as se:
            await session.rollback()
            raise se
        finally:
            await session.close()
