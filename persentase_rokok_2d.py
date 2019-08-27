import numpy as np
import matplotlib.pyplot as plt
import csv

all=[]
with open('Persentase Perokok RI.csv', 'r') as x:
    reader = csv.DictReader(x)
    for i in reader:
        all.append(dict(i))

Provinsi=[]
Tahun_2015=[]
Tahun_2016=[]
for i in all:
    Provinsi.append(i['Provinsi'])
    Tahun_2015.append(float((i['2015'])))
    Tahun_2016.append(float((i['2016'])))
# print(Provinsi)

labels = Provinsi
y = Tahun_2015
z = Tahun_2016
y = np.array(y)
z = np.array(z)
x = np.arange(len(labels)) 
width = 0.35

fig, ax = plt.subplots()

ax.bar(x - width/2, y, width, label='2015')
ax.bar(x + width/2, z, width, label='2016')
plt.subplots_adjust(bottom=.41)

ax.set_ylabel('Percentage')
ax.set_title('Percentage by Province and Year')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=90)

ax.legend()
# plt.savefig('inigrafikku.png')
plt.show()