# Python Training

## Numer BOOM.py
 Guess number game, will tell you range<br>
 If you guess the boom number, the game will over!<br>
1. Set your Boom number range
2. Guess number
3. Decrease number range and guess again


## CrawlBug_GameSale.py
 This is a crawl bug function.<br>
 Crawling Second-hand price of the TV game on PTT GameSale page<br>
 web=https://www.ptt.cc/bbs/Gamesale/<br>

First-time use should be
* install python
* pip install xlwt
* pip install prettytable
 
操作說明 - 在Define中設定<br>
  * PLACE="台北"   //設定想搜尋地區<br>
  * SearchName="織夢島"  //設定想搜尋的遊戲<br>
  * Days="2"    //搜尋幾天內的文，default Days =0
  * Page=0      //搜尋幾頁內的文，default page =0
  
### 2019.12.16
 * Add:search Articles in a few Days
 * Add:Output results in Execl (.csv)

### 2019.12.13
 * Add:能設定位置、頁面數、遊戲名來搜尋資料
 * Add:最終列出 Name, Price, Place, Url 表格
 

未來想加入功能
* (完成)~~搜尋幾天內的文~~
* 濾掉同PO文者的文- 比對ID及標題<br>


## CrawlBug_TrainDelay.py
 This is a crawl bug function.<br>
 Crawling delay time for taiwan's train<br>
 web="https://www.railway.gov.tw/tra-tip-web/tip" (Taiwan's train official website)
 
 操作說明<br>
* Station="松山"      ex.臺北 臺中("臺"要繁體字)
* direction="往北"    ex.south or north 往北or往南 
 
 
### 2019.12.13
 * 指定車站、方向，依現在時間列出後面的班次列車
 * 顯示 班車編號、到站時間、終點站、延誤時間
 
 未來想加入功能
 * 顯示更晚時間的delay time ，may be version II
 * 新增輸入user目的地，篩選可搭的車輛

## CrawlBug_TrainDelay II.py
 This is a crawl bug function.<br>
 Crawling delay time for taiwan's train<br>
 This is different of original version on that can show more detail currect delay time <br>
 web="http://train.ptx.fly.idv.tw/"


