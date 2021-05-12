from pydantic import BaseSettings


class Settings(BaseSettings):
    API_ENDPOINT: str = "/api"
    PROJECT_NAME: str = "push-gateway"

    class Config:
        case_sensitive = True


settings = Settings()
