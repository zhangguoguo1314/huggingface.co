import os
from pathlib import Path

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "Account-Auto-Sign"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # HuggingFace Spaces 只有 /data 和 /tmp 可写
    # 本地开发时使用 ./data.db，HuggingFace 使用 /data/data.db
    DATABASE_URL: str = "sqlite:///./data.db"

    # Email settings
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: Optional[str] = None

    # Playwright settings
    PLAYWRIGHT_HEADLESS: bool = True

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()

# HuggingFace Spaces: /data 目录可写，/app 只读
# 如果 /data 目录存在，强制使用 /data/data.db
if os.path.isdir("/data"):
    settings.DATABASE_URL = "sqlite:////data/data.db"
