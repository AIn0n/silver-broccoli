from fastapi import APIRouter
from models.device import Device, EnergyClass, DeviceType
from config.db import conn

device = APIRouter()


@device.post("/{room}/device")
def add_new_device(room: str, device: Device):
    if len(device.name) < 1:
      return {"message" : "cannot add device - empty name"}
    conn["database"]["rooms"].update_one(
        {"name": room}, {"$push": {"devices": dict(device)}}
    )
    return {"message": "successfully added new device <3"}


@device.get("/energy-class")
def get_all_possible_energy_classes():
    return {member.name: member.value for member in EnergyClass}


@device.get("/device-type")
def get_all_device_classes():
    return {it.name: it.value for it in DeviceType}
