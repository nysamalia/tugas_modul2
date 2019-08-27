import csv
import mysql.connector

dataCsv = []
with open ('data.csv','r') as x:
    reader= csv.DictReader(x)
    for i in reader:
       dataCsv.append(dict(i))



# dbku = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     password = '12345678',
#     auth_plugin = 'mysql_native_password'
    
# )

# kursor = dbku.cursor()
# # kursor.execute("create database new")
# kursor.execute("use new")
# # querydb='''create table karakter(
# #     id int not null auto_increment, 
# #     nama varchar(30),
# #     usia smallint,
# #     primary key (id)
# # )
# # '''
# # kursor.execute(querydb)

dataMsql = []
for i in range (0, len(dataCsv)):
    data = []
    for k in dataCsv[i].keys():
        data.append(dataCsv[i][k])
    dataMsql.append(tuple(data))
print(dataMsql)
# querydb = '''
# insert into karakter(id, nama, usia) values  (%s, %s, %s)
# '''

# kursor.executemany(querydb,dataMsql)
# dbku.commit()
