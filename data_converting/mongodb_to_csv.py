import pymongo
import csv

x = pymongo.MongoClient('mongodb://localhost:27017')

db = x['marvel']
col = db['avengers']

datacsv = list(col.find())
kolom = list(datacsv[0].keys())

with open ('darimongodb.csv', 'w', newline='') as x:
    writer = csv.DictWriter(x,fieldnames=kolom)
    writer.writeheader()
    writer.writerows(datacsv)