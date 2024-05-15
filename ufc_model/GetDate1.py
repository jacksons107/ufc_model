#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 00:35:57 2021

@author: Jackson
"""


import requests
from bs4 import BeautifulSoup

URL = 'http://ufcstats.com/event-details/e49c2db95e572dc8'

def get_date(URL):
    '''
     -input: url of specific card page
        -from: get_fight_link_list
    -output: date from that card
        -to: excel writer
    '''
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    date_list = []
    for li in soup.find_all('li', {'class':'b-list__box-list-item'}):
        date_list.append(" ".join(li.text.split()))
        
    date = date_list[0]
    date= date.replace('Date: ', '')
    
    return date

print(get_date(URL))


