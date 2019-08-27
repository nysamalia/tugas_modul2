import json
import mysql.connector

datajson = []
with open ('datajson.json','r') as x:
    reader = json.load(x)
    for i in reader:
        datajson.append(i)


dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '12345678',
    auth_plugin = 'mysql_native_password'
)

kursor = dbku.cursor()
# kursor.execute("create database darijson")
kursor.execute("use darijson")
querydb='''create table karakter(
    id varchar(30) not null, 
    usia smallint,
    title varchar(30),
    primary key (id)
)
'''
kursor.execute(querydb)

dataMsql = []
for i in range (0, len(datajson)):
    data = []
    for k in datajson[i].keys():
        data.append(datajson[i][k])
    dataMsql.append(tuple(data))



querydb = '''
insert into karakter(id, usia, title) values  (%s, %s, %s)
'''

kursor.executemany(querydb,dataMsql)
dbku.commit()
