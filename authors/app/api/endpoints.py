from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from app.api import crud, deps, push, schemas
from app.db.repository import Repository

router = APIRouter()


@router.get("/", response_model=List[schemas.AuthorInDBBase])
def get_authors(db: Repository = Depends(deps.get_db)) -> Any:
    """
    Retrieve authors list.
    """
    authors = crud.author.get_multi(db=db)
    return authors


@router.get("/{id}", response_model=schemas.AuthorInDBBase)
def get_author_by_id(
    *,
    db: Repository = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get author by ID
    """
    result = crud.author.get(db=db, id=id)
    if not result:
        raise HTTPException(status_code=404, detail="Author not found")
    return result


@router.post("/", response_model=schemas.AuthorInDBBase)
def create_author(
    *,
    db: Repository = Depends(deps.get_db),
    author_in: schemas.AuthorCreate,
) -> Any:
    """
    Create new author.
    """
    result = crud.author.create(db=db, obj_in=author_in)
    push.send_push(result.dict())
    return result
