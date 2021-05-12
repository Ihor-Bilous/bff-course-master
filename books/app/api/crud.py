from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from app.api import schemas
from app.db.repository import Repository

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[BaseModel]) -> None:
        self.model = model

    def get(self, db: Repository, id: Any) -> Optional[BaseModel]:
        return db.get_by_id(self.model, id)

    def get_multi(self, db: Repository) -> List[BaseModel]:
        return [item for item in db.all(self.model)]

    def create(self, db: Repository, obj_in: CreateSchemaType) -> BaseModel:
        obj_in_data = jsonable_encoder(obj_in)
        new_id = db.get_max_id(self.model) + 1
        db_obj = self.model(id=new_id, **obj_in_data)  # type: ignore
        db.add(db_obj)
        return db_obj

    def update(self, db: Repository, db_obj: BaseModel, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> BaseModel:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        updated_obj = self.model(id=getattr(db_obj, "id"), **update_data)  # type: ignore
        db.add(updated_obj)
        return updated_obj

    def remove(self, db: Repository, id: int) -> Optional[BaseModel]:
        obj = db.get_by_id(self.model, id)
        if obj:
            db.remove(obj)
        return obj


class CRUDAuthor(CRUDBase[schemas.BookCreate, schemas.BookUpdate]):
    pass


book = CRUDAuthor(schemas.BookInDBBase)
