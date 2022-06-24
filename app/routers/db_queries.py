from sqlmodel import Session, select
from .models import Users, Sessions
import app


def get_users() -> list[Users]:
    with Session(app.db_engine) as session:
        statement = select(Users)
        users = session.exec(statement).all()
        return users


def get_user_by_email(email: str) -> Users:
    with Session(app.db_engine) as session:
        statement = select(Users).where(Users.email == email)
        user = session.exec(statement).one()
        return user


def save_session(user_session: Sessions):
    with Session(app.db_engine) as session:
        session.add(user_session)
        session.commit()
        session.refresh(user_session)
