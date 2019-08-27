import csv
import json

#buka data csv
data = []
with open ('fileku.csv', 'r') as x:
    reader= csv.DictReader(x)
    for i in reader:
       data.append(dict(i))

with open ('fileku.json','w') as x:
    json.dump(data,x)
