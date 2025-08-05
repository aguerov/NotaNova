from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..database import engine
from ..models import Reminder

router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@router.get("/", response_model=list[Reminder])
def read_reminders(session: Session = Depends(get_session)):
    return session.exec(select(Reminder)).all()


@router.post("/", response_model=Reminder)
def create_reminder(reminder: Reminder, session: Session = Depends(get_session)):
    session.add(reminder)
    session.commit()
    session.refresh(reminder)
    return reminder
