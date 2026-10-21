
from pathlib import Path

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_env: str

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

try:
    settings = Settings()
except ValidationError:
    raise RuntimeError(
        "CampusHub configuration is invalid. "
        "Set the required APP_ENV variable in your .env file "
        "or environment before starting the application."
    )from None



