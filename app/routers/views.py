from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

import app.routers.db_queries as db
from app.db import db_session, get_session
from app.routers.models import Users
from app.routers.schemas import SignInQuery, RefreshTokensQuery
import app.routers.auth_functions as af
from sqlmodel import Session

auth_router = APIRouter()


@auth_router.get('/users', response_model=list[Users])
def users(*, session: Session = Depends(get_session)):
    db_session.set(session)
    db_users = db.get_users()
    return db_users


@auth_router.post('/sign_in')
def sign_in(*, session: Session = Depends(get_session), sign_in_data: SignInQuery):
    db_session.set(session)

    user_session = af.sign_in(sign_in_data)
    user_session_dict = af.get_sign_in_response(user_session)
    return JSONResponse(content=user_session_dict)


@auth_router.post('/refresh_tokens')
def refresh_tokens(*, session: Session = Depends(get_session), refresh_tokens_data: RefreshTokensQuery):
    db_session.set(session)
    user_session = af.refresh_tokens(refresh_tokens_data)
    user_session_dict = af.get_sign_in_response(user_session)
    return JSONResponse(content=user_session_dict)
