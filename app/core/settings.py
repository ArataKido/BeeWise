from fastapi import HTTPException
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from pydantic import ValidationError
import logging


from app.utils import raise_exception
from app.core.base import AbsctractSettings
from app.core.db import make_async_session, start_async_engine


class Settings(AbsctractSettings):
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgresPass@database_beewise:5432/quiz"
    )
    DATABASE_NAME: str = None
    DATABASE_USER: Optional[str] = None
    DATABASE_HOST: Optional[str] = None
    DATABASE_PORT: Optional[str | int] = None
    DATABASE_PASSWORD: Optional[str] = None
    engine: AsyncEngine
    Session: AsyncSession

    @classmethod
    async def start(
        cls,
        DATABASE_NAME: str = None,
        DATABASE_USER: str = None,
        DATABASE_PASSWORD: str = None,
        DATABASE_HOST: str = None,
        DATABASE_PORT: str = None,
        DATABASE_URL: str = None,
    ) -> None:
        """
        Firstly, try loads from envirement, then from function arguments,`
        then from settings defaults.

        see plugins.AbsctractSettings.loads_secrets for more
        """

        (
            DATABASE_NAME,
            DATABASE_USER,
            DATABASE_PASSWORD,
            DATABASE_HOST,
            DATABASE_PORT,
            DATABASE_URL,
        ) = cls.loads_secrets(
            DATABASE_NAME=DATABASE_NAME,
            DATABASE_USER=DATABASE_USER,
            DATABASE_PASSWORD=DATABASE_PASSWORD,
            DATABASE_HOST=DATABASE_HOST,
            DATABASE_PORT=DATABASE_PORT,
            DATABASE_URL=DATABASE_URL,
        )

        cls.engine = await start_async_engine(cls.DATABASE_URL)
        cls.Session = await make_async_session(cls.engine)

    @classmethod
    def get_session(cls):
        def decorator(func):
            async def wrapper(*args, **kwargs):
                try:
                    if kwargs.get("session", None):
                        return await func(*args, **kwargs)
                    else:
                        async with cls.Session() as session:
                            result = await func(*args, session=session, **kwargs)
                    return result
                except ValidationError as e:
                    raise_exception(e)
                except HTTPException as e:
                    raise_exception(e)
                except Exception as e:
                    logging.exception(e)

            return wrapper

        return decorator
