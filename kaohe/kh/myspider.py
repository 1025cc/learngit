# -*- coding:utf-8 -*-#
import requests
import argparse
from bs4 import BeautifulSoup
from kh.models import Date,Weather,Temperature

def start():
    date1 = []
    weather1 = []
    temperature1 = []
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
        date1.append(unicode(item.string).encode('utf-8'))
    for item in soup("img", {"class": 'icons0_wt'}):
        weather1.append(item['alt'].encode('utf-8'))
    for item in soup('p', class_='wt_fc_c0_i_temp'):
        temperature1.append(item.string.encode('utf-8'))
    for i in range(9):
        d = Date()
        d.date = date1[i]
        d.save()
        w = Weather()
        w.day = weather1[i * 2]
        w.night = weather1[i * 2 + 1]
        w.save()
        t = Temperature()
        t.temp = temperature1[i]
        t.save()
if __name__ == "__main__":
    start()
    print('Done!')


