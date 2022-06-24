from pydantic import Field, EmailStr, Extra, BaseModel, SecretStr

import config


class Query(BaseModel):
    class Config:
        extra = Extra.forbid


class SignInQuery(Query):
    email: EmailStr
    password: SecretStr = Field(
        min_length=config.MIN_PASSWORD_LENGTH,
        max_length=config.MAX_PASSWORD_LENGTH
    )
