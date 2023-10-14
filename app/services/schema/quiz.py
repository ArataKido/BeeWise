from pydantic import BaseModel
from datetime import datetime


class QuizQuestionSchema(BaseModel):
    question_id: int
    question: str
    answer: str
    created_at: datetime
