from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    first_name: str
    second_name: str
    last_name: str
    password_hash: str

    sessions: list["Sessions"] = Relationship(back_populates="user")


class Sessions(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    access_token: str
    refresh_token: str
    access_expiration_date: datetime
    refresh_expiration_date: datetime

    user_id: int = Field(default=None, foreign_key="users.id")
    user: Users = Relationship(back_populates="sessions")

    class Config:
        fields = {'id': {'exclude': True},
                  'user_id': {'exclude': True}}
