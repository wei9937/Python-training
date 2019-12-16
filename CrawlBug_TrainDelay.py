import urllib
import requests
from bs4 import BeautifulSoup
import sys
import re
from prettytable import PrettyTable
from prettytable import from_csv
import prettytable as pt
import datetime
import csv
import pandas as pd


print("Train Delay Time!")

####    Define info     #####
Station="松山"      #臺北 臺中
direction="往北"    # south or north 往北or往南


###########################

#取得今日時間
today=datetime.datetime.today()  
if today.day<10:
    day="0"+str(today.day)
    date=str(today.year)+"/"+str(today.month)+"/"+day
    print("Today = "+str(today.month)+"/"+day)
else:
    day=str(today.day)
    date=str(today.year)+"/"+str(today.month)+"/"+str(today.day)
    print("Today ="+str(today.month)+"/"+str(today.day))


s = requests.session() #取得Request Session

#web="https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystationblank?rideDate=2019/11/01&station=0990-%E6%9D%BE%E5%B1%B1"

web="https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobystation"

res = s.get(web) #取得HTML頁面
soup = BeautifulSoup(res.text, 'html.parser') #將抓回的HTML頁面傳入BeautifulSoup，使用html.parser解析
div_tags = soup.find_all('button', {'class': 'btn tipStation'}) #找到網頁中全部的 <div class="title">
#soup.find('div','date')
#print(div_tags)

list_station=[]
list_name=[]
list_all_info=[]

for div_tag in div_tags:
    #a_tag = div_tag.find('title') #找到 <div class="title"> 下的 <a>
    tag=div_tag.get('title')    #取得 title=下的訊息
    list_station.append(tag)
    list_name.append(div_tag.text)
    #print(div_tag.text)
    
print("總站數="+str(len(list_station)))    
index=list_name.index(Station)
Station=list_station[index]
print("台北站="+Station)



delay_web="https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystationblank?rideDate="+date+"&station="+Station
print(delay_web)
res = s.get(delay_web) #取得HTML頁面
soup = BeautifulSoup(res.text, 'html.parser') #將抓回的HTML頁面傳入BeautifulSoup，使用html.parser解析
if direction=="往北":
    div_tags = soup.find_all('div', {'class': 'tab-pane active'}) #找到網頁中全部的 <table class="itinerary-controls">
else :
    div_tags = soup.find_all('div', {'class': 'tab-pane'}) #找到網頁中全部的 <div class="tab-pane">

table = PrettyTable(["Number", "Arive Time","Destination ", "Delay Time"])

#soup.find('div','date')

print("Today = "+str(today.month)+"/"+day+" Time="+str(today.hour)+":"+str(today.minute))
if today.hour<10:
    timenow="0"+str(today.hour)+":"+str(today.minute)
else:
    timenow=str(today.hour)+":"+str(today.minute)

print("Time="+timenow)

for div_tag in div_tags:
    #a_tag = div_tag.find('tbody') #找到 <div class="title"> 下的 <a>
    
    number=div_tag.find('a')
    #table.add_row(number)
    tag=div_tag.find('div','note')
    tag=div_tag.find_all('tr')


    for i in range(2,len(tag)):
        
        text = str(tag[i].text).replace('\n',' ')
        
        info = text.split(" ")

        number=info[6]
        time=info[10]
        destination=info[11]
        #print("info 長度:"+str(len(info)))
        #print("info 長度:"+str(len(info))+"，delay="+info[17])
        if len(info)>18:
            delay=info[17]+info[18]
        else:
            delay="NULL"
            #print("info 17:"+info[17])

        hour=time.split(":")
        if today.hour<=int(hour[0]):
            table.add_row([number, time, destination, delay])
            
        #print("time = "+str(time))
        
    
    abc=str(div_tag.text).replace("\n"," ")
    #print(abc+"\n")
print(table)

with open("Delay.csv","w",newline="") as datacsv:

    csvwriter=csv.writer(datacsv,dialect=("execl"))
    csvwriter.writerow(["A","B","C","D"])

#from prettytable import from_csv
#fp = open("test1.csv", "r")
#tb1 = from_csv(fp)
#fp.close()

#for i in range(0,len(info)):
 #   print("info "+str(i)+" ="+str(info[i]))
