from database import Connection
import json
import csv
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

def getData():
    cursor = Connection()
    cursor.execute("exec [dbo].[SP_AVERAGE_PRICE_CATTLE_SUMMARY]")
    rows = cursor.fetchall()
    cattleList = []
    for row in rows:
        cattleList.append({"Year": row[0], "Month": row[1], "Gender": row[2], "Price": row[3]})
    return cattleList


def create_csv(json_data):
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
    
    
def calculate_prediction(csv_path):
    
    df = pandas.read_csv(csv_path)

    gender_q = {'Female': 0, 'Male': 1}
    df['Gender'] = df['Gender'].map(gender_q)


    attributes = ['Year','Month','Gender']
    x = df[attributes]
    y = df['Price']

    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(x.values, y) 
    
    return dtree


def predict(dtree, item):
    result = int(dtree.predict([[item.year, item.month, item.gender]]))
    return result
    
