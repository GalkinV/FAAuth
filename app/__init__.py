from fastapi import FastAPI


import app.routers.views as view


app = FastAPI()
app.include_router(view.auth_router)



