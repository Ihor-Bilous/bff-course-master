from typing import List

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    pages: int
    author_id: int
    genres: List[str]


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookInDBBase(BookBase):
    id: int

    class Config:
        orm_mode = True
