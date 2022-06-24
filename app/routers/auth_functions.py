import os
from datetime import datetime

import config
from app.routers.models import Users, Sessions
from app.routers.schemas import SignInQuery
import app.routers.db_queries as db
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import HTTPException
import binascii


def sign_in(sign_in_data: SignInQuery) -> str:
    user = db.get_user_by_email(sign_in_data.email)

    if not check_password_hash(user.password_hash, sign_in_data.password.get_secret_value()):
        raise HTTPException(status_code=403, detail="Incorrect email or password.")

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
