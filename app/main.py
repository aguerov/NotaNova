from fastapi import FastAPI

from .routers import notes, reminders
from .database import create_db_and_tables

app = FastAPI(title="NotaNova")

app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(reminders.router, prefix="/reminders", tags=["reminders"])


@app.on_event("startup")
def on_startup() -> None:
    """Create database tables on startup."""
    create_db_and_tables()
