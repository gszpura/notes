from pydantic import BaseModel
from notes_backend.modules.note.models import Note


class NoteDisplay(BaseModel):
    id: int
    note: str
    created_at: str
    updated_at: str

    @staticmethod
    def from_db_note(note: Note):
        return NoteDisplay(
            id=note.id,
            note=note.note,
            created_at=note.created_at.strftime("%m/%d/%Y %H:%M:%S"),
            updated_at=note.updated_at.strftime("%m/%d/%Y %H:%M:%S")
        )


class NotesResponse(BaseModel):
    notes: list[NoteDisplay] | None = []


class NoteAddRequest(BaseModel):
    note: str
