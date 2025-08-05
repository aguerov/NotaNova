from fastapi import FastAPI

from .models import Note, Reminder

app = FastAPI(title="NotaNova Demo")

notes: list[Note] = []
reminders: list[Reminder] = []

_note_id_counter = 1
_reminder_id_counter = 1


@app.get("/notes", response_model=list[Note])
def read_notes() -> list[Note]:
    return notes


@app.post("/notes", response_model=Note)
def create_note(note: Note) -> Note:
    global _note_id_counter
    note.id = _note_id_counter
    _note_id_counter += 1
    notes.append(note)
    return note


@app.get("/reminders", response_model=list[Reminder])
def read_reminders() -> list[Reminder]:
    return reminders


@app.post("/reminders", response_model=Reminder)
def create_reminder(reminder: Reminder) -> Reminder:
    global _reminder_id_counter
    reminder.id = _reminder_id_counter
    _reminder_id_counter += 1
    reminders.append(reminder)
    return reminder
