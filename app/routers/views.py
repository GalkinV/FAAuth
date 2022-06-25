from fastapi import APIRouter
from starlette.responses import JSONResponse

import app.routers.db_queries as db
from app.routers.models import Users
from app.routers.schemas import SignInQuery, RefreshTokensQuery
import app.routers.auth_functions as af

auth_router = APIRouter()


@auth_router.get('/users', response_model=list[Users])
def users():
    db_users = db.get_users()
    return db_users


@auth_router.post('/sign_in')
def sign_in(sign_in_data: SignInQuery):
    user_session = af.sign_in(sign_in_data)
    user_session_dict = af.get_sign_in_response(user_session)
    return JSONResponse(content=user_session_dict)


@auth_router.post('/refresh_tokens')
def refresh_tokens(refresh_tokens_data: RefreshTokensQuery):
    user_session = af.refresh_tokens(refresh_tokens_data)
    user_session_dict = af.get_sign_in_response(user_session)
    return JSONResponse(content=user_session_dict)
