from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.settings import Settings


def start_async_engine() -> Engine:
    return create_engine(Settings.db_url)


def make_async_session(engine: Engine) -> Session:
    if engine is None:
        engine = start_async_engine()
    return sessionmaker(engine)
