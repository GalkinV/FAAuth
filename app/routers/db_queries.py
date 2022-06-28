from sqlalchemy.orm import joinedload
from sqlmodel import Session, select
from .models import Users, Sessions, Companies
import app


def get_users() -> list[Users]:
    with Session(app.db_engine) as session:
        statement = select(Users)
        users = session.exec(statement).all()
        return users


def get_user_by_email(email: str) -> Users:
    with Session(app.db_engine) as session:
        statement = select(Users).where(Users.email == email)
        user = session.exec(statement).first()
        return user


def save_session(user_session: Sessions):
    with Session(app.db_engine) as session:
        session.add(user_session)
        session.commit()
        session.refresh(user_session)


def get_session_by(**kwargs) -> Sessions:
    with Session(app.db_engine) as session:
        statement = select(Sessions).filter_by(**kwargs).options(joinedload(Sessions.user))
        user_session = session.exec(statement).first()
        return user_session


def get_company(company_id: int) -> Companies:
    with Session(app.db_engine) as session:
        statement = select(Companies).where(Companies.id == company_id)
        company = session.exec(statement).first()
        return company
