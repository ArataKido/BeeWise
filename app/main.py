from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from app.core.settings import DatabaseSettings, Database
from app.routers import quiz


app = FastAPI(
    title="Quiz Microservice",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz.router, prefix="/quiz")


# @app.on_event("startup")
# async def create_sessions() -> None:
#     db_settings = DatabaseSettings(
#         db_name=os.environ["DATABASE_NAME"],
#         db_user=os.environ["DATABASE_USER"],
#         db_password=os.environ["DATABASE_PASSWORD"],
#         db_hostname=os.environ["DATABASE_HOST"],
#         db_port=os.environ["DATABASE_PORT"],
#     )
#     db = Database(params=db_settings)
