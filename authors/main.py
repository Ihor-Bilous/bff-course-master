from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.api import api_router
from app.core.config import settings
from app.db.repository import Repository, init_db

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_ENDPOINT}/openapi.json")

app.include_router(api_router, prefix=settings.API_ENDPOINT)

init_db(Repository)


@app.middleware("http")
async def authentication_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")
    if not token:
        return JSONResponse(status_code=401, content={"detail": "Missing authorization token"})    
    if token != settings.AUTH_TOKEN:
        return JSONResponse(status_code=401, content={"detail": "Authorization token is invalid"})
    return await call_next(request)
