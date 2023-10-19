from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class QuizQuestionSchema(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime
    updated_at: datetime
    airdate: datetime
    category_id: int
    game_id: int
    value: Optional[int] = None
    invalid_count: Optional[bool] = None
