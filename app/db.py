from sqlmodel import create_engine, Session
from contextvars import ContextVar

from config import Settings

db_engine = create_engine(Settings().DATABASE_URL)
# db_engine = create_engine(Settings().DATABASE_URL, echo=True)


def get_session():
    with Session(db_engine) as session:
        print("-------session", session)
        yield session
    print('----close session')


db_session: ContextVar[Session] = ContextVar('db_session')
