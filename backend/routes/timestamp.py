from fastapi import APIRouter
from models.timestamp import Timestamp
from config.db import collection

timestamp = APIRouter()

@timestamp.post("/{room}/device/{device}/timestamp")
def add_timestamp(room: str, device: str, timestamp: Timestamp):
  collection.update_one(
    {"name": room, "devices.name": device},
    {
      "$push" : { "devices.$.timestamps": dict(timestamp)}
    }
  )
  return {"message" : "sucessfully added timestamp"}