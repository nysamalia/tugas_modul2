import csv
import pymongo

dataCsv = []
with open ('data.csv','r') as x:
    reader= csv.DictReader(x)
    for i in reader:
       dataCsv.append(dict(i))

p = pymongo.MongoClient('mongodb://localhost:27017')
db = p['daricsvkemongo']
col = db['doraemon']

add = col.insert_many(dataCsv)
print(add.inserted_ids)
