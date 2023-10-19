from fastapi import APIRouter

from app.controllers.quiz import make_request, add_questions
from app.services.schema.quiz import QuizQuestionSchema

router = APIRouter()


@router.post("/bring_questions")
async def parce_questions(
    questions_num: int,
) -> QuizQuestionSchema | None:
    if questions := make_request(questions_num=questions_num):
        return await add_questions(questions)


# @router.post("/bring_questions")
# async def parce_questions(
#     questions_num: int,
# ) -> QuizQuestionSchema | None:
#     if questions := make_request(questions_num=questions_num):
# @router.post("/bring_questions")
# async def parce_questions(
#     questions_num: int,
# ) -> QuizQuestionSchema | None:
#     if questions := make_request(questions_num=questions_num):
