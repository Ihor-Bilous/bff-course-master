from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings
from app.db.repository import Repository, init_db

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_ENDPOINT}/openapi.json")

app.include_router(api_router, prefix=settings.API_ENDPOINT)

init_db(Repository)
