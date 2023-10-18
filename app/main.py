from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import Settings
from app.core.db import start_async_engine, make_async_session
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
    engine = await start_async_engine()
    session = await make_async_session(engine=engine)

    Settings.engine = engine
    Settings.Session = session


# @app.on_event("shutdown")
# async def close_asyncpg_session():
#     await Settings.engine.dispose()
