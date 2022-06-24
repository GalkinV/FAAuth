import os

from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel

import app.routers.views as view

app = FastAPI()
app.include_router(view.auth_router)

DATABASE_URL = os.environ.get("DATABASE_URL")
db_engine = create_engine(DATABASE_URL)
