import pyodbc
from pydantic import BaseModel


class ConnectionData(BaseModel):
    server = 'DESKTOP-MTRG5DU'
    database = 'Cattle'
    username = 'steven'
    password = '1234'


def Connection():
    data = ConnectionData()
    cnxn = pyodbc.connect('DRIVER={SQL Server};' +
                          'SERVER='+data.server +
                          ';DATABASE='+data.database +
                          ';UID='+data.username +
                          ';PWD=' + data.password)
    print("Conexion Exitosa")
    cursor = cnxn.cursor()
    return cursor


# def getData():
#     cursor = Connection()
#     cursor.execute("exec [dbo].[SP_AVERAGE_PRICE_CATTLE_SUMMARY]")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
        

# Connection()
# getData()
