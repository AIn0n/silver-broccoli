from fastapi import APIRouter
from models.room import Room
from config.db import conn
from schemas.room import roomEntity

room = APIRouter()


@room.get("/")
async def find_all_rooms():
    return [roomEntity(room) for room in conn["database"]["rooms"].find()]


@room.post("/")
async def create_room(room: Room):
    conn["database"]["rooms"].insert_one(dict(room))
    return {"message": "OK"}
