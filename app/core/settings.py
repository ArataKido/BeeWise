# from pydantic_settings import BaseSettings
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from pydantic import ValidationError

from fastapi import HTTPException

from app.utils import raise_exception

import logging


class Settings:
    db_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/quiz"
    db_name: str = "quiz"
    db_user: Optional[str] = "postgres"
    db_host: Optional[str] = "database_beewise"
    db_port: Optional[int or str] = 5432
    db_password: Optional[str] = "postgresPass"

    engine: AsyncEngine
    Session: AsyncSession

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
