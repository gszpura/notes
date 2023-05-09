from notes_backend.core.logger import logger
from notes_backend.setup_app import create_app, settings


app = create_app()


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting uvicorn")
    uvicorn.run(
        "main:app",
        host=settings.UVICORN_HOST,
        reload=settings.is_dev(),
        port=settings.UVICORN_PORT,
    )