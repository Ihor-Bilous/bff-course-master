from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    born: str


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class AuthorInDBBase(AuthorBase):
    id: int

    class Config:
        orm_mode = True
