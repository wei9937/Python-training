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


web="http://train.ptx.fly.idv.tw/"

s = requests.session() #取得Request Session

res = s.get(web) #取得HTML頁面
soup = BeautifulSoup(res.text, 'html.parser') #將抓回的HTML頁面傳入BeautifulSoup，使用html.parser解析


div_tags = soup.find_all('option', {'vlu': 'btn tipStation'}) #找到網頁中全部的 <div class="title">
print(div_tags)





