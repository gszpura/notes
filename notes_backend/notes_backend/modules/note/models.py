from pydantic import BaseModel
import datetime


# TODO: maybe use SQLModel lib?
class Note(BaseModel):
    id: int
    note: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
