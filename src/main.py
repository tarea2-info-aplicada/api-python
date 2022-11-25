
from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
import services as services
import os

app = FastAPI()


class Item(BaseModel):
    year: int
    month: int
    gender: int


@app.post("/")
async def getDataCattle(request: Request):

    file = './data_cattle.csv'

    print('+++++++++++++ DATOS REcibidos desde C# +++++++++++++')
    result = await request.json()
    item = Item(year=result['year'],
                month=result['month'],
                gender=result['gender'])
    
    if (os.path.exists(file)):
        print("csv existe")
        csv_path = './data_cattle.csv'
        dtree = services.calculate_prediction(csv_path)
        result = services.predict(dtree, item)
    else:
        print("csv no existe")
        json_data = services.getData()
        services.create_csv(json_data)
        csv_path = './data_cattle.csv'
        dtree = services.calculate_prediction(csv_path)
        result = services.predict(dtree, item)
        
    print("Resultado: ")
    print(result)

    return result

@app.get("/")
def index():
    return "py server started"
