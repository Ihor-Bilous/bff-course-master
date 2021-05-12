from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from app.api import crud, deps, push, schemas
from app.db.repository import Repository

router = APIRouter()


@router.get("/", response_model=List[schemas.BookInDBBase])
def get_books(db: Repository = Depends(deps.get_db)) -> Any:
    """
    Retrieve books list.
    """
    authors = crud.book.get_multi(db=db)
    return authors


@router.get("/{id}", response_model=schemas.BookInDBBase)
def get_author_by_id(
    *,
    db: Repository = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get book by ID
    """
    result = crud.book.get(db=db, id=id)
    if not result:
        raise HTTPException(status_code=404, detail="Author not found")
    return result


@router.post("/", response_model=schemas.BookInDBBase)
def create_author(
    *,
    db: Repository = Depends(deps.get_db),
    author_in: schemas.BookCreate,
) -> Any:
    """
    Create new book.
    """
    result = crud.book.create(db=db, obj_in=author_in)
    push.send_push(result.dict())
    return result
