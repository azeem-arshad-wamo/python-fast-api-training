from fastapi import FastAPI
from routes import basic, users, extras

app = FastAPI()

app.include_router(basic.router)
app.include_router(users.router)
app.include_router(extras.router)