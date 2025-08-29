import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    host: str
    port: int
    api_prefix: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_DRIVER_ASYNC: str
    POSTGRES_PORT: int

    pgadmin_default_email: str
    pgadmin_default_password: str

    @property
    def db_uri(self) -> str:
        return (
            f"postgresql+{self.POSTGRES_DRIVER_ASYNC}://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
