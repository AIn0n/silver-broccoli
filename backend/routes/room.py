from fastapi import APIRouter
from models.room import Room
from config.db import conn
from schemas.room import roomEntity
from pymongo.errors import DuplicateKeyError

room = APIRouter()


@room.get("/room/")
async def find_all_rooms():
    return [roomEntity(room) for room in conn["database"]["rooms"].find()]


@room.post("/room/")
async def create_room(room: Room):
    if len(room.name) < 1:
        return {"message": "room name is empty"}
    try:
        conn["database"]["rooms"].insert_one(dict(room))
    except DuplicateKeyError:
        return {"message": "room already exists"}
    return {"message": "OK"}
