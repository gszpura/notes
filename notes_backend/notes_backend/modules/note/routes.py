from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from notes_backend.core.config import settings
from notes_backend.core.schema import DefaultResponse
from notes_backend.modules.note.api_schema import NoteAddRequest, NotesResponse, NoteDisplay
from notes_backend.db.session import get_db
from notes_backend.modules.note.models import Note


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
def root() -> dict:
    return {
        "status": True,
        "msg": "Project information",
        "details": {
            "name": f"{settings.PROJECT_NAME}",
            "version": f"{settings.APP_VERSION}",
        },
    }


@router.get("/notes", status_code=status.HTTP_200_OK, response_model=NotesResponse)
async def get_notes(db: AsyncSession = Depends(get_db)) -> NotesResponse:
    notes: list[Note] = []
    print(notes)
    response_cursor = await db.execute("SELECT * FROM notes ORDER BY created_at DESC")

    for note in response_cursor:
        notes.append(NoteDisplay.from_db_note(note))
    return NotesResponse(notes=notes)


@router.post("/note", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
async def add_note(request: NoteAddRequest, db: AsyncSession = Depends(get_db)) -> DefaultResponse:
    # TODO: ofc escape it, or use SQLModel
    await db.execute(f"INSERT INTO notes(note) VALUES ('{request.note}')")
    await db.commit()
    return DefaultResponse(status=True, msg="ok")
