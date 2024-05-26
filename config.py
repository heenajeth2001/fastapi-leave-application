from pydantic import AnyHttpUrl, EmailStr, validator
from typing import List, Optional, Union
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V2_STR: str = "/api"
    JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PROD"
    ALGORITHM: str = "HS256"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

settings = Settings()