from sqlalchemy.sql.expression import select, insert, exists
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

from app.services.models.quiz import QuizQuestionModel
from app.services.schema.quiz import QuizQuestionSchema
from app.core.settings import Settings


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


@Settings.get_session()
async def question_exists(session: AsyncSession, question_id: int) -> bool:
    stmt = exists(
        select(QuizQuestionModel).where(QuizQuestionModel.id == question_id)
    ).select()
    result = (await session.execute(stmt)).scalars().first()
    return result


@Settings.get_session()
async def create(session: AsyncSession, **values: Any) -> QuizQuestionModel:
    stmt = (
        insert(QuizQuestionModel)
        .values(QuizQuestionSchema(**values).model_dump())
        .returning(QuizQuestionModel)
    )
    result = (await session.execute(stmt)).scalars().first()
    await session.commit()
    return result


@Settings.get_session()
async def get(
    model: QuizQuestionModel, session: AsyncSession, **values: Any
) -> QuizQuestionModel:
    stmt = select(QuizQuestionModel).where(**values)
    return (await session.execute(stmt)).scalars().first()
