# -*- coding:utf-8 -*-#
import requests
import re
import argparse
from bs4 import BeautifulSoup
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
date = []
weather = []
temperature = []
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--city', default='wuhan')
args = parser.parse_args()
city = args.city
url = 'http://weather.sina.com.cn/' + city
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
city = soup.find(class_='slider_ct_name').string.encode('utf-8')
for item in soup('p', class_='wt_fc_c0_i_date'):
    date.append(unicode(item.string).encode('utf-8'))
for item in soup("img", {"class": 'icons0_wt'}):
    weather.append(item['alt'].encode('utf-8'))
for item in soup('p', class_='wt_fc_c0_i_temp'):
    temperature.append(item.string.encode('utf-8'))
conn = MySQLdb.connect(host='localhost', user='root', passwd='2c2c!!', db='kaohe', charset='utf8')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS weatherdata")
sql = 'CREATE TABLE IF NOT EXISTS weatherdata(date DATE,day VARCHAR(40) NOT NULL,night VARCHAR(40) NOT NULL,temperature VARCHAR(40) NOT NULL );'
cursor.execute(sql)
for counter in range(9):
    date1=date[counter]
    day1=weather[2*counter]
    night1=weather[2*counter+1]
    temp1=temperature[counter]
    sql_insert='insert into weatherdata(date,day,night) values (%s,%s,%s)'%(date1,day1,night1)
    try:
        cursor.execute(sql_insert)
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
conn.close()
