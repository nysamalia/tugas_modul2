import csv
import json


data = []
with open ('data.json','r') as x:
    reader = json.load(x)
    for i in reader:
        data.append(i)


with open ('darijson.csv', 'w', newline='') as x:
    kolom = list(data[0].keys())
    writer = csv.DictWriter(x,fieldnames=kolom)
    writer.writeheader()
    writer.writerows(data)