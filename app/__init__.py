from fastapi import FastAPI
from sqlmodel import create_engine

import app.routers.views as view
from config import Settings

app = FastAPI()
app.include_router(view.auth_router)


db_engine = create_engine(Settings().DATABASE_URL)

