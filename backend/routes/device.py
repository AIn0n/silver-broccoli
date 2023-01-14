from fastapi import APIRouter
from models.device import Device, EnergyClass, DeviceType
from schemas.device import device_entity
from config.db import conn

device = APIRouter()


def retrieve_devices_from_room(room: str) -> list:
    return map(
        lambda n: device_entity(n),
        conn["database"]["rooms"].find_one({"name": room})["devices"],
    )


@device.post("/{room}/device")
def add_new_device(room: str, device: Device):
    # check if devices exist
    if device.name in map(lambda x: x["name"], retrieve_devices_from_room(room)):
        return {"message": "device already created"}
    if len(device.name) < 1:
        return {"message": "cannot add device - empty name"}
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
