import json
import pymongo

datajson = []
with open ('data.json','r') as x:
    reader = json.load(x)
    for i in reader:
        datajson.append(i)


p = pymongo.MongoClient('mongodb://localhost:27017')

#bikin db & collection
db = p['darijsonkemongo']
col = db['doraemon']


add = col.insert_many(datajson)
print(add.inserted_ids)



