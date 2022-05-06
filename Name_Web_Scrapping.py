import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup



r = requests.get('https://www.iplt20.com/teams/mumbai-indians/squad/2022')
content = r.content.decode(encoding='UTF-8')
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")

names = soup.find_all('div', {"class": "ih-p-name"})
# names = soup.find_all('p', {"class": "ih-p-img"})

name=[]

for item in names:
    name.append(item.text)

# print(len(name))
print(name)
print(len(name))
# pp = [1,4,17,18] Mumbai Ind 2017
# pp =[15,16,19] chennai 
# pp =[6,22] dc 
# pp = [6,7] kkr 2018
# pp=[12,19] #pbks 2018
# pp =[15]# RCB 2018
# pp = [14,23] srh 2018
# pp =[6,18,20] RR 2018
pp = [11]
cnt =0
for i in pp:
    name.pop(i-cnt)
    cnt += 1
print(len(name))
print(name)


pl = ["D:\IPL\PlayerImages\Aaa0.jpg"
,"D:\IPL\PlayerImages\Aaa1.jpg"
,"D:\IPL\PlayerImages\Aaa2.jpg"
,"D:\IPL\PlayerImages\Aaa3.jpg"
,"D:\IPL\PlayerImages\Aaa4.jpg"
,"D:\IPL\PlayerImages\Aaa5.jpg"
,"D:\IPL\PlayerImages\Aaa6.jpg"
,"D:\IPL\PlayerImages\Aaa7.jpg"
,"D:\IPL\PlayerImages\Aaa8.jpg"
,"D:\IPL\PlayerImages\Aaa9.jpg"
,"D:\IPL\PlayerImages\Aaa10.jpg"
,"D:\IPL\PlayerImages\Aaa11.jpg"
,"D:\IPL\PlayerImages\Aaa12.jpg"
,"D:\IPL\PlayerImages\Aaa13.jpg"
,"D:\IPL\PlayerImages\Aaa14.jpg"
,"D:\IPL\PlayerImages\Aaa15.jpg"
,"D:\IPL\PlayerImages\Aaa16.jpg"
,"D:\IPL\PlayerImages\Aaa17.jpg"
,"D:\IPL\PlayerImages\Aaa18.jpg"
,"D:\IPL\PlayerImages\Aaa19.jpg"
,"D:\IPL\PlayerImages\Aaa20.jpg"
,"D:\IPL\PlayerImages\Aaa21.jpg"
,"D:\IPL\PlayerImages\Aaa22.jpg"
,"D:\IPL\PlayerImages\Aaa23.jpg"
,"D:\IPL\PlayerImages\Aaa24.jpg"
]

import os 
def renameImges(pl):
    for i,pl in enumerate(pl):
        n = name[i] 
        # print(n)
        n = n[1:len(n)-1]
        n = n.replace(' ','_')
        print(n)
        # new = old
        # print(i, pl)
        new = pl.split('Aa')[0]+  n+".jpg"
        os.rename(pl,new )

renameImges(pl)