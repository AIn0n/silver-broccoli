from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class Item(BaseModel):
  name: str
  decription: Optional[str] = None
  price: float
  tax: Optional[float] = None

@app.post("/items/")
async def root(item: Item):
    return os.getenv("MONGO_URL")
