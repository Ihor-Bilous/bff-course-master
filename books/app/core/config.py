from pydantic import BaseSettings


class Settings(BaseSettings):
    API_ENDPOINT: str = "/api"
    PROJECT_NAME: str = "books"
    REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        case_sensitive = True


settings = Settings()
