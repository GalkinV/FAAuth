from fastapi import APIRouter

import app.routers.db_queries as db
from app.routers.models import Users
from app.routers.schemas import SignInQuery
import app.routers.auth_functions as af

auth_router = APIRouter()


@auth_router.get('/users', response_model=list[Users])
def users():
    db_users = db.get_users()
    return db_users


@auth_router.post('/sign_in')
def sign_in(sign_in_data: SignInQuery):
    return af.sign_in(sign_in_data)
