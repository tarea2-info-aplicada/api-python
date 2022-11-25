from database import Connection
import json
import csv
import os
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier


def getData():
    cursor = Connection()
    cursor.execute("exec [dbo].[SP_AVERAGE_PRICE_CATTLE_SUMMARY]")
    rows = cursor.fetchall()
    cattleList = []
    for row in rows:
        cattleList.append(
            {"Year": row[0], "Month": row[1], "Gender": row[2], "Price": row[3]})
    return cattleList


def create_csv(json_data):
    print("creando csv...")
    write_csv = open('./data_cattle.csv', 'w')
    csv_writer = csv.writer(write_csv)

    count = 0

    for item in json_data:
        if count == 0:
            header = item.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(item.values())
    write_csv.close()
    print("csv creado...")


def calculate_prediction(csv_path):

    print("leyendo csv...")
    df = pandas.read_csv(csv_path)

    gender_q = {'Female': 0, 'Male': 1}
    df['Gender'] = df['Gender'].map(gender_q)

    attributes = ['Year', 'Month', 'Gender']
    x = df[attributes]
    y = df['Price']
    
    print("creando arbol de decision...")
    dtree = DecisionTreeClassifier()
    print("Arbol creado...")
    print("Evaluando datos...")
    dtree = dtree.fit(x.values, y)
    
    os.remove('./data_cattle.csv')
    print("csv eliminado")

    return dtree


def predict(dtree, item):
    print("Obteniendo prediccion...")
    result = int(dtree.predict([[item.year, item.month, item.gender]]))
    return result
