from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import Settings
from app.core.db import start_async_engine, make_async_session
from app.routers import quiz

# from app.core.configs import settings, api_token_manager

# from plugins.cache.base import CacheManagerBase


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

# settings.api_token = api_token_manager.encode(
#     {'name': app.title}


@app.on_event("startup")
async def create_connections_pool():
    # await DatabaseManager.start(
    #     settings.POSTGRES_DB,
    #     settings.POSTGRES_USER,
    #     settings.POSTGRES_PASSWORD,
    #     settings.POSTGRES_HOST,
    # )
    engine = start_async_engine()
    session = make_async_session(engine=engine)

    Settings.session = session


# @app.on_event("shutdown")
# async def close_asyncio_client():
#     await settings.aiohttp_session.close()


# @app.on_event("shutdown")
# async def close_connections_pool():
#     await Configs.CONNECT_POOL.close()
