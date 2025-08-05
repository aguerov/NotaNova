import os
from typing import Any, Dict

from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./notanova.db")
connect_args: Dict[str, Any] = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def create_db_and_tables() -> None:
    """Create database tables."""
    SQLModel.metadata.create_all(engine)
