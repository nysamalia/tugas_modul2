import mysql.connector
import json


dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '12345678',
    auth_plugin = 'mysql_native_password',
    database = 'doraemon'
)

kursor = dbku.cursor()

querydb_kolom = '''describe haha
'''
kursor.execute(querydb_kolom)
datajson = []
kolom = []
for i in (kursor.fetchall()):
    kolom.append(i[0])

querydb_data = '''select*from haha
'''
kursor.execute(querydb_data)
val = kursor.fetchall()

for i in range(0, len(val)):
    data = {}
    for j in range (0, len(kolom)):
        data.update({kolom[j]:val[i][j]})
    datajson.append(data)

with open ('darimysql.json', 'w', newline='') as x:
    json.dump(datajson,x)
    