from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
