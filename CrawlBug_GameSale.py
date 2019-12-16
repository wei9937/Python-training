import urllib
import requests
from bs4 import BeautifulSoup
import sys
import xlwt
import re
import csv
from prettytable import PrettyTable
import datetime

#rideDate=sys.argv[1];
#station=sys.argv[2];

#---------------      Define       -------------------#
Price=""
PLACE="台北"
SearchName="寶可夢"
Url=""
Days="1"            # 搜尋幾天內的文，default Days =0
Page=0              # 搜尋幾頁內的文，default page =0
#-----------------------------------------------------#

s = requests.session() #取得Request Session
#通過檢查是否超過18歲的頁面
s.post('https://www.ptt.cc/ask/over18', 
          data = {'from': '/bbs/Beauty/index.html', 'yes': 'yes'})
web="https://www.ptt.cc/bbs/Gamesale/search?q=NS"

search=SearchName


#取得今日時間  
today=datetime.datetime.today()  
if today.day<10:
    day="0"+str(today.day)
    date=str(today.month)+"/"+day
else :
    day=str(today.day)
    date=str(today.month)+"/"+day
print("Today = "+str(today.month)+"/"+day)

a=1     #當前頁面
table = PrettyTable(["Name", "Price","Place", "Url"])


while a != -1: 
    if (Page==0 and Days==0):    #若無設定搜尋條件
        print("Please setting the searched config !")
        break
    else:
        print("Setting comfirm : Page="+str(Page)+", Days="+str(Days))            
        
    web="https://www.ptt.cc/bbs/Gamesale/search?page="+str(a)+"&q="+str(search)
    res = s.get(web) #取得HTML頁面
    #print(res.text) #印出取回的HTML內容

    soup = BeautifulSoup(res.text, 'html.parser') #將抓回的HTML頁面傳入BeautifulSoup，使用html.parser解析
    div_tags = soup.find_all('div', {'class': 'title'}) #找到網頁中全部的 <div class="title">
    #print(soup)
    #day_tags = soup.find_all('div',{'class':'date'})
   
    #print(today)

    for div_tag in div_tags:

        #判斷是不是符合日期
        if int(Days)>0:
            #for i in (int Days)
            last_date= today-datetime.timedelta(days=int(Days)) 
            if last_date.day<10:    #個位數天數時加0
                ldate=str(last_date.month)+"/0"+str(last_date.day)
            else:
                ldate=str(last_date.month)+"/"+str(last_date.day)

            page_date=soup.find('div','date').string
            print("ldate="+str(ldate)+", page_date="+str(page_date))
            
            if page_date <= ldate:
                print("Break")
                a=-1
                break;
        
        #print(str(day_tags[div_tag]))
        a_tag = div_tag.find('a') #找到 <div class="title"> 下的 <a>

        split = re.split(r'[;,\"]\s*',str(a_tag))
        link="https://www.ptt.cc"+split[1]

        res2 = s.get(link)
        soup2 = BeautifulSoup(res2.text, 'lxml') #將抓回的HTML頁面傳入BeautifulSoup，使用html.parser解析
        #print(res2.text)
        info_tags = soup2.find(id="main-content").text
        
        target_text=u'【售    價】：'
        content = info_tags.split(target_text)
        #print(len(content))
        if len(content)>1:
            price=content[1].split('★')
            target="（販售者填寫，不得超過定價，海外商品價格請參考板規二。）"
            price=price[0].split(target)
            price=price[0].replace(' ',"")
            price=price.replace('\n'," ")
        else:
            price="沒有售價"

        target_text=u'【地    區】：'
        content = info_tags.split(target_text)
        #print(len(content))
        if len(content)>1:
            place=content[1].split('\n')
        else:
            place="無"
            
        #print(info_tags)
        
        if a_tag is not None: #或文章被刪除會是None，所以要排除None
            #print(a_tag.text) #印出文字部分
            #print(a_tag.text+"\t 價格:"+link) #印出文字部分
            if place[0].find(PLACE)!=-1: #搜尋地區
                table.add_row([a_tag.text, price, place[0], link])
                #myWriter.writerow([a_tag.text, price, place[0], link])


    if a == Page: 
        a=-1
        break;
    if a!=-1:              
        a=a+1

#將table資料載入至 Excel
with open(r'gamesale.csv','w',newline='') as myFile:
 myWriter = csv.writer(myFile)
 myWriter.writerow(["Name", "Price","Place", "Url"])
 for row in table:
    row.border = False
    row.header = False
    row.align = "c"
    row.valign = "m"

    name = row.get_string(fields=["Name"])
    price = row.get_string(fields=["Price"])
    place = row.get_string(fields=["Place"])
    url = row.get_string(fields=["Url"])
    mylist = [name,price,place,url]
    myWriter.writerow(mylist)
    
 myFile.close()


table.reversesort = True
print(table)
