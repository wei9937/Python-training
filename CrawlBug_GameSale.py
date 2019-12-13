import urllib
import requests
from bs4 import BeautifulSoup
import sys
import re
from prettytable import PrettyTable
import datetime

#rideDate=sys.argv[1];
#station=sys.argv[2];

##      Define 
Prize=""
PLACE="台北"
SearchName="織夢島"
Url=""
Date="2" #搜尋幾天內的文
################################################


s = requests.session() #取得Request Session


#通過檢查是否超過18歲的頁面
s.post('https://www.ptt.cc/ask/over18', 
          data = {'from': '/bbs/Beauty/index.html', 'yes': 'yes'})

web="https://www.ptt.cc/bbs/Gamesale/search?q=NS"
web2="https://www.ptt.cc/bbs/Gamesale/search?page=2&q=NS"
#web="https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystationblank?rideDate=2019/11/01&station=0990-%E6%9D%BE%E5%B1%B1"
search=SearchName

a=1
table = PrettyTable(["Name", "Prize","Place", "Url"])
while a < 3: 
    web="https://www.ptt.cc/bbs/Gamesale/search?page="+str(a)+"&q="+str(search)
    res = s.get(web) #取得HTML頁面
    #print(res.text) #印出取回的HTML內容

    soup = BeautifulSoup(res.text, 'html.parser') #將抓回的HTML頁面傳入BeautifulSoup，使用html.parser解析
    #div_tags = soup.find_all('td') #找到網頁中全部的 <div class="title">
    div_tags = soup.find_all('div', {'class': 'title'}) #找到網頁中全部的 <div class="title">
    #print(div_tags)

    #取得今日時間
    today=datetime.datetime.today()  
    if today.day<10:
        day="0"+str(today.day)
        date=str(today.month)+"/"+day
    print("Today = "+str(today.month)+"/"+day)
    #print(today)

    for div_tag in div_tags:

        #判斷是不是符合日期
        '''if soup.find('div','date').string=="12/05" :
            print("Today")
        else:
            print("Not today")
            break;
'''
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
            prize=content[1].split('★')
            target="（販售者填寫，不得超過定價，海外商品價格請參考板規二。）"
            prize=prize[0].split(target)
            prize=prize[0].replace(' ',"")
            prize=prize.replace('\n'," ")
        else:
            prize="沒有售價"

        target_text=u'【地    區】：'
        content = info_tags.split(target_text)
        #print(len(content))
        if len(content)>1:
            place=content[1].split('\n')
        else:
            place="無"
            
        #print(info_tags)
        #link = div_tag.find('href')
        if a_tag is not None: #或文章被刪除會是None，所以要排除None
            #print(a_tag.text) #印出文字部分
            #print(a_tag.text+"\t 價格:"+link) #印出文字部分
            if place[0].find(PLACE)!=-1: #搜尋地區
                table.add_row([a_tag.text, prize, place[0], link])
           
    a=a+1

table.reversesort = True
print(table)


#火車
#train = s.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystationblank?rideDate=2019/11/01&station=0990-%E6%9D%BE%E5%B1%B1');
#print(train.text);


