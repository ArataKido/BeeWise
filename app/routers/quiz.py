from fastapi import APIRouter

from app.services.schema.quiz import QuizQuestionSchema
from app.controllers.quiz import make_request, add_questions

router = APIRouter()


@router.post("/bring_questions")
def parce_questions(
    questions_num: int,
):
    print("this0")
    if questions := make_request(questions_num=questions_num):
        return add_questions(questions)
    return questions_num
