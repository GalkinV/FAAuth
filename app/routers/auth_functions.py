import os
from datetime import datetime

import config
from app.routers.models import Users, Sessions
from app.routers.schemas import SignInQuery, RefreshTokensQuery
import app.routers.db_queries as db
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import HTTPException
import binascii


def sign_in(sign_in_data: SignInQuery) -> Sessions:
    user = db.get_user_by_email(sign_in_data.email)

    if not check_password_hash(user.password_hash, sign_in_data.password.get_secret_value()):
        raise HTTPException(status_code=403, detail="Incorrect email or password.")

    validate_user(user)

    session = create_session(user)
    return session


def generate_token(length: int = config.TOKEN_LENGTH) -> str:
    return binascii.hexlify(os.urandom(round(length / 2))).decode()[:length]


def create_session(user: Users):
    user_session = Sessions(user=user,
                            access_token=generate_token(),
                            access_expiration_date=datetime.utcnow() + config.ACCESS_TOKEN_TTL,
                            refresh_token=generate_token(),
                            refresh_expiration_date=datetime.utcnow() + config.REFRESH_TOKEN_TTL)
    db.save_session(user_session)
    return user_session


def refresh_session(session: Sessions):
    session.access_token = generate_token()
    session.access_expiration_date = datetime.utcnow() + config.ACCESS_TOKEN_TTL
    session.refresh_token = generate_token()
    session.refresh_expiration_date = datetime.utcnow() + config.REFRESH_TOKEN_TTL
    db.save_session(session)
    return session


def get_sign_in_response(session: Sessions) -> dict:
    resp = {
        'access_token': session.access_token,
        'access_token_expires_in': config.ACCESS_TOKEN_TTL.total_seconds(),
        'refresh_token': session.refresh_token,
        'refresh_token_expires_in': config.REFRESH_TOKEN_TTL.total_seconds(),
    }
    return resp


def refresh_tokens(refresh_tokens_data: RefreshTokensQuery):
    user_session = db.get_session_by(refresh_token=refresh_tokens_data.refresh_token)

    if user_session is None or user_session.refresh_expiration_date < datetime.utcnow():
        raise HTTPException(status_code=401, detail="The session does not exist or has expired.")

    validate_user(user_session.user)
    user_session = refresh_session(user_session)
    return user_session


def validate_user(user: Users):
    user_company = db.get_company(user.company_id)
    if user_company is None:
        is_valid_user = user.active_flag == 1
    else:
        is_valid_user = user.active_flag == 1 and user_company.active_flag
    if not is_valid_user:
        raise HTTPException(status_code=403, detail="Invalid user.")

