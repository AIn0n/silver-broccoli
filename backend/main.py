from fastapi import FastAPI
from routes.room import room
from routes.device import device
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

app.include_router(room)
app.include_router(device)
