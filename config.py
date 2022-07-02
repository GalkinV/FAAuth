import os
from datetime import timedelta
from pydantic import constr, BaseSettings, PostgresDsn

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 255

ACCESS_TOKEN_TTL = timedelta(hours=1)
REFRESH_TOKEN_TTL = timedelta(days=10)

TOKEN_LENGTH = 80

TOKEN_PATTERN = constr(
    strip_whitespace=True,
    strict=True,
    min_length=TOKEN_LENGTH,
    max_length=TOKEN_LENGTH
)


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
