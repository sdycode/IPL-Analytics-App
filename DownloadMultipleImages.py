
from email import header
from wsgiref import headers
from bs4 import BeautifulSoup
import requests
import urllib.request

# 


# 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


source = requests.get('https://www.iplt20.com/teams/mumbai-indians/squad/2022', headers=headers).text
soup = BeautifulSoup(source,'lxml')
# src="https://assets.iplt20.com/ipl/IPLHeadshot2022/107.png"
Images=[]
img_links = soup.select('img[src^="https://assets.iplt20.com/ipl/IPLHeadshot2022/"]')
# img_links = soup.select('img[src^="https://bcciplayerimages.s3.ap-south-1.amazonaws.com/playerheadshot/ipl/210/"]')
for i in range(len(img_links)):
    Images.append(img_links[i]['src'])
    print("ajsk")
for i in range(len(Images)):
    name="D:/IPL/PlayerImages/"+str("Aaa")+str(i)+".jpg"
    urllib.request.urlretrieve(Images[i],name)

# https://bcciplayerimages.s3.ap-south-1.amazonaws.com/playerheadshot/ipl/210/211.png
# https://bcciplayerimages.s3.ap-south-1.amazonaws.com/playerheadshot/ipl/210/1748.png


# https://www.iplt20.com/assets/images/default-headshot.png