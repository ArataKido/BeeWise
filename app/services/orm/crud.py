from sqlalchemy.sql.expression import select, insert, exists
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any
from fastapi import Depends

from app.services.models.quiz import QuizQuestionModel
from app.services.schema.quiz import QuizQuestionSchema
from app.core.settings import get_db


async def model_to_schema(question: AsyncSession) -> QuizQuestionSchema:
    return QuizQuestionSchema(
        id=question.id,
        question=question.question,
        answer=question.answer,
        created_at=question.created_at,
        saved_at=question.saved_at,
        airdate=question.airdate,
        invalid_count=question.invalid_count,
        category_id=question.category_id,
        game_id=question.game_id,
        updated_at=question.updated_at,
        value=question.value,
    )


async def question_exists(
    question_id: int, session: AsyncSession = Depends(get_db)
) -> bool:
    stmt = exists(
        select(QuizQuestionModel).where(QuizQuestionModel.id == question_id)
    ).select()
    result = (await session.execute(stmt)).scalars().first()
    return result


async def create(
    session: AsyncSession = Depends(get_db), **values: Any
) -> QuizQuestionModel:
    dumped_values = QuizQuestionSchema(**values).model_dump()
    stmt = insert(QuizQuestionModel).values(dumped_values).returning(QuizQuestionModel)
    result = (await session.execute(stmt)).scalars().first()
    await session.commit()
    return result


async def get(
    session: AsyncSession = Depends(get_db), **values: Any
) -> QuizQuestionModel:
    stmt = select(QuizQuestionModel).where(**values)
    return (await session.execute(stmt)).scalars().first()
