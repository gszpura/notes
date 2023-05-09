from pydantic import BaseModel


class NotesResponse(BaseModel):
    notes: list[str] | None = []

