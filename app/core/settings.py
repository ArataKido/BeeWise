# from pydantic_settings import BaseSettings
from typing import Optional
from sqlalchemy.orm import Session
from pydantic import ValidationError

from fastapi import HTTPException

from app.utils import raise_exception

import logging


class Settings:
    db_url: str = "postgresql+psycopg2://postgres:postgresPass@database_beewise:5432/quiz"
    db_name: str = "quiz"
    db_user: Optional[str] = "postgres"
    db_host: Optional[str] = "database_beewise"
    db_port: Optional[int or str] = 5432
    db_password: Optional[str] = "postgresPass"

    session: Session = None

    @classmethod
    def get_session(cls):
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    if kwargs.get("session", None):
                        return func(*args, **kwargs)
                    else:
                        with cls.session() as session:
                            result = func(*args, session=session, **kwargs)
                    return result
                except ValidationError as e:
                    raise_exception(e)
                except HTTPException as e:
                    raise_exception(e)
                except Exception as e:
                    logging.exception(e)

            return wrapper

        return decorator
