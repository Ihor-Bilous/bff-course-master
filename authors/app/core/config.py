from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_ENDPOINT: str = "/api"
    PROJECT_NAME: str = "authors"
    NOTIFICATION_URL: Optional[str]
    AUTH_TOKEN: str = ""

    class Config:
        case_sensitive = True


settings = Settings()
