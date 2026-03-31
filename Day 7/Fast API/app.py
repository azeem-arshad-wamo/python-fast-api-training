from fastapi import FastAPI, Query
from typing import Annotated
from routes.query import router as queryRouter
from routes.path import router as pathRouter
from routes.body import router as bodyRouter
from routes.examples import router as exampleRouter

app = FastAPI()

app.include_router(queryRouter)
app.include_router(pathRouter)
app.include_router(bodyRouter)
app.include_router(exampleRouter)