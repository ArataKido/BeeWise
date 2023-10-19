from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.controllers.quiz import make_request, add_questions
from app.services.schema.quiz import QuizQuestionSchema

router = APIRouter()


@router.post("/parce_questions")
async def parce_questions(
    questions_num: int,
) -> QuizQuestionSchema | None:
    """questions_num cant be more than 100!"""
    if not questions_num > 100:
        if questions := make_request(questions_num=questions_num):
            return await add_questions(questions)
    return JSONResponse(
        status_code=400, content={"message": "Questions_Num cant be greater than 100"}
    )
