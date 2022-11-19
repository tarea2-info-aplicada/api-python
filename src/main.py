
from fastapi import FastAPI
from pydantic import BaseModel

import services as services

app = FastAPI()

class Item(BaseModel):
    Year: int
    Month: int
    Gender: int


@app.post("/")
def getDataCattle(item: Item):
    
    json_data = services.getData()
    services.create_csv(json_data)
    csv_path = './data_cattle.csv'
    dtree = services.calculate_prediction(csv_path)
    result = services.predict(dtree, item)

    return result
