#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 23:39:10 2021

@author: Jackson
"""

import requests
from bs4 import BeautifulSoup

URL = 'http://ufcstats.com/event-details/e49c2db95e572dc8'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

def get_winners(URL):

    fighter_list = []
    for a in soup.find_all('a', {'class':'b-link b-link_style_black'}):
        fighter_list.append(" ".join(a.text.split()))
        
    winner_list = []
    for i in range(len(fighter_list)):
        if i%2 == 0:
            winner_list.append(fighter_list[i])
        
    return winner_list
    
    
def get_losers(URL):
    fighter_list = []
    for a in soup.find_all('a', {'class':'b-link b-link_style_black'}):
        fighter_list.append(" ".join(a.text.split()))
    
    loser_list = []
    for i in range(len(fighter_list)):
        if i%2 != 0:
            loser_list.append(fighter_list[i])
        
    return loser_list

print(get_winners(URL))
print(get_losers(URL))