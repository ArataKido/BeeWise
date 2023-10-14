from datetime import datetime
from typing import Optional
from sqlalchemy import Integer, DateTime, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True
    __name__: Mapped[str]

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BaseWithID:
    """Base model class that represents ID with an integer type"""

    id: Mapped[Optional[int]] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        nullable=False,
    )


class BaseWithTime:
    created_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        onupdate=func.now(),
        server_default=func.now(),
    )
