from sqlalchemy.orm import Session
import requests

from app.services.models.quiz import QuizQuestionModel
from app.services.schema.quiz import QuizQuestionSchema
from app.core.settings import Settings


def model_to_schema(question: QuizQuestionModel) -> QuizQuestionSchema:
    return QuizQuestionSchema(
        question_id=question.question_id,
        question=question.question,
        answer=question.answer,
        created_at=question.created_at,
    )


@Settings.get_session()
def select(question: dict, session: Session) -> int:
    question_exists = (
        session.query(QuizQuestionModel).filter_by(question_id=question["id"]).count()
        > 0
    )
    return question_exists


@Settings.get_session()
def create(question: dict, session: Session):
    query = QuizQuestionModel(
        question_id=question["id"],
        question=question["question"],
        answer=question["answer"],
        created_at=question["created_at"],
        updated_at=question["updated_at"],
    )
    session.add(query)
    session.commit()


@Settings.get_session()
def select_last_saved(session: Session) -> QuizQuestionSchema:
    last_question = (
        session.query(QuizQuestionModel)
        .order_by(QuizQuestionModel.saved_at.desc())
        .first()
    )
    return model_to_schema(last_question)


def add_questions(questions: list):
    for question in questions:
        if select(question) is False:
            create(question)
    return select_last_saved()


def make_request(questions_num: int):
    response = requests.get(url=f"https://jservice.io/api/random?count={questions_num}")
    if response is not None and response.status_code != 400 or 404:
        return response.json()
    return False
