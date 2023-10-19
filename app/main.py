from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from app.core.settings import Settings
from app.routers import quiz


app = FastAPI(
    title="Quiz Microservice",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


Settings.APP = app


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz.router, prefix="/quiz")


@app.on_event("startup")
async def create_connections_pool():
    await Settings.start(
        DATABASE_HOST=os.getenv("DATABASE_HOST"),
        DATABASE_NAME=os.getenv("DATABASE_NAME"),
        DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD"),
        DATABASE_USER=os.getenv("DATABASE_USER"),
        DATABASE_URL=os.getenv("DATABASE_URL"),
        DATABASE_PORT=os.getenv("DATABASE_PORT"),
    )


# @app.on_event("shutdown")
# async def close_asyncpg_session():
