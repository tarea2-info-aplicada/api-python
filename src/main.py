
from fastapi import FastAPI
from services import CattleServices
from pydantic import BaseModel

import json

app = FastAPI()


class Item(BaseModel):
    Year: int
    Month: int
    Weight: str
    Gender: str
    Price = float


@app.get("/", response_model=list[Item])
async def getData():
    services = CattleServices()
    list = await services.getData()
    print(list)
    return list
