from typing import Generator

from app.db.repository import Repository


def get_db() -> Generator:
    db = Repository
    yield db
