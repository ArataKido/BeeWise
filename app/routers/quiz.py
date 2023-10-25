from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.quiz import make_request, add_questions
from app.services.schema.quiz import QuizQuestionSchema
from app.core.settings import get_db

router = APIRouter()


@router.post("/parce_questions")
async def parce_questions(
    questions_num: int,
    session: AsyncSession = Depends(get_db)
) -> QuizQuestionSchema | None:
    """questions_num cant be more than 100!"""
    if not questions_num > 100:
        if questions := make_request(questions_num=questions_num):
            return await add_questions(questions=questions, session=session)
    return JSONResponse(
        status_code=400, content={"message": "Questions_Num cant be greater than 100"}
    )
