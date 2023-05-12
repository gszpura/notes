from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from notes_backend.core.config import settings
from notes_backend.core.logger import logger
from notes_backend.routes import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.APP_VERSION,
        docs_url=None if settings.is_prod() else "/docs",
        redoc_url=None if settings.is_prod() else "/redoc",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )
    setup_routers(app)
    setup_middlewares(app)
    Instrumentator().instrument(app).expose(app)
    return app


def setup_routers(app: FastAPI) -> None:
    app.include_router(api_router, prefix=settings.API_V1_STR)
    logger.info(f"Routes:\n {api_router.routes}")


def setup_middlewares(app) -> None:
    # TODO: setup logging/metrics middleware

    origins = []

    # Set all CORS enabled origins : adding security between Backend and Frontend
    if settings.BACKEND_CORS_ORIGINS:
        origins_raw = settings.BACKEND_CORS_ORIGINS.split(",")

        for origin in origins_raw:
            use_origin = origin.strip()
            origins.append(use_origin)

        print(origins)
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3000"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
