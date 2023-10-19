from app.services.models.base import Base, BaseWithTime
from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from datetime import datetime


class QuizQuestionModel(Base, BaseWithTime):
    id: Mapped[int] = mapped_column(
        nullable=False, primary_key=True, index=True, unique=True
    )
    question: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[int] = mapped_column(nullable=True)
    category_id: Mapped[int] = mapped_column(nullable=False)
    game_id: Mapped[int] = mapped_column(nullable=False)
    invalid_count: Mapped[Optional[bool]] = mapped_column(nullable=True)
    saved_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    airdate: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
