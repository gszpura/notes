from fastapi import APIRouter
from notes_backend.modules.note.routes import router as note_router


api_router = APIRouter()
api_router.include_router(note_router, tags=["Note"])
