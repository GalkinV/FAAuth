from sqlalchemy.orm import joinedload
from sqlmodel import select
from .models import Users, Sessions, Companies
from app.db import db_session


def get_users() -> list[Users]:
    context_session = db_session.get()
    statement = select(Users)
    users = context_session.exec(statement).all()
    return users


def get_user_by_email(email: str) -> Users:
    context_session = db_session.get()
    statement = select(Users).where(Users.email == email)
    user = context_session.exec(statement).first()
    return user


def save_session(user_session: Sessions):
    context_session = db_session.get()
    context_session.add(user_session)
    context_session.commit()
    context_session.refresh(user_session)


def get_session_by(**kwargs) -> Sessions:
    context_session = db_session.get()
    statement = select(Sessions).filter_by(**kwargs).options(joinedload(Sessions.user))
    user_session = context_session.exec(statement).first()
    return user_session


def get_company(company_id: int) -> Companies:
    context_session = db_session.get()
    statement = select(Companies).where(Companies.id == company_id)
    company = context_session.exec(statement).first()
    return company
