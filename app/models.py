from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str = ""


class Reminder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    note_id: Optional[int] = Field(default=None, foreign_key="note.id")
    remind_at: Optional[datetime] = None
    location: Optional[str] = None
