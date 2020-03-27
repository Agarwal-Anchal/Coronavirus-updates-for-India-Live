import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt

extracts=lambda row: [x.text.replace('\n','') for x in row]
URL = 'https://www.mohfw.gov.in/'

Short_Headers=['Sn','State','Indian Confirmed','Foreign Confirmed','Cured','Death']
response=requests.get(URL).content
soup=BeautifulSoup(response, 'html.parser')
header= extracts(soup.tr.find_all('th'))

stats=[]
all_rows=soup.find_all('tr')

for row in all_rows:
        stat=extracts(row.find_all('td'))
        if stat:
            if len(stat) ==5:
                    stat=['',*stat]
                    stats.append(stat)
            elif len(stat)==6:
                    stats.append(stat)
stats[-1][1]='Total cases'
stats.remove(stats[-1])

objects=[]
for row in stats:
        objects.append(row[1])
y_pos=np.arange(len(objects))
performance=[]
for row in stats:
        performance.append(int(row[2])+int(row[3]))

table= tabulate(stats, headers=Short_Headers)
print(table)

plt.barh(y_pos,performance,align='center',alpha=0.5,color=(234/256.0,128/256.0,252/256.0),edgecolor=(106/256.0,27/256.0,154/256.0))
plt.yticks(y_pos,objects)
plt.xlim(1,max(performance))
plt.grid()
plt.xlabel("Number of Cases")
plt.title('Corona Virus Cases')
plt.show()
