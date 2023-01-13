from fastapi import FastAPI
from routes.room import room

app = FastAPI()
app.include_router(room)
