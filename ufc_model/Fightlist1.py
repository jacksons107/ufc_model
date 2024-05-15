#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:45:05 2021

@author: Jackson
"""


import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/List_of_UFC_events'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

for a in soup.find_all('a', href=True):
    print(a['href'])
