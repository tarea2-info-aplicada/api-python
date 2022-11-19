
from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
import services as services

app = FastAPI()

class Item(BaseModel):
    year: int
    month: int
    gender: int


@app.post("/")
async def getDataCattle(request: Request):
    
    print('+++++++++++++ DATOS REcibidos desde C# +++++++++++++')
    result = await request.json()
    item = Item(year=result['year'],
                month=result['month'],
                gender=result['gender'])

    json_data = services.getData()
    services.create_csv(json_data)
    csv_path = './data_cattle.csv'
    dtree = services.calculate_prediction(csv_path)
    result = services.predict(dtree, item)
    
    print("Resultado: ")
    print(result)

    return result
