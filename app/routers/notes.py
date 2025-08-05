from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..database import engine
from ..models import Note

router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@router.get("/", response_model=list[Note])
def read_notes(session: Session = Depends(get_session)):
    return session.exec(select(Note)).all()


@router.post("/", response_model=Note)
def create_note(note: Note, session: Session = Depends(get_session)):
    session.add(note)
    session.commit()
    session.refresh(note)
    return note
