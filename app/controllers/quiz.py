import requests
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.orm.crud import create, question_exists, model_to_schema


def make_request(questions_num: int):
    response = requests.get(
        url=f"https://jservice.io/api/random?count={questions_num}", timeout=60
    )
    if response is not None and response.status_code != 400 or 404:
        return response.json()
    return False


async def add_questions(questions: list, session: AsyncSession):
    last_created = None
    for question in questions:
        _question_exists = await question_exists(
            question_id=question["id"], session=session
        )
        if not _question_exists:
            last_created = await create(session=session, **question)
        if _question_exists:
            new_question = make_request(1)
            await add_questions(new_question, session=session)
    if last_created:
        return await model_to_schema(last_created)
    return last_created
