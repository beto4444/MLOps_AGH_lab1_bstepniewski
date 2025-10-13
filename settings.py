# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        ...  # implement me!
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        allowed = {"dev", "test", "prod"}
        if value not in allowed:
            raise ValueError(f"Wrong environment: {value!r}, must be one of {allowed}")
        return value
