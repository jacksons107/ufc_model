#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:45:38 2020

@author: Jackson
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:10:12 2020

@author: Jackson
"""


import requests
from bs4 import BeautifulSoup
import string


URL = 'http://ufcstats.com/fighter-details/4b4fc3ddc307bc73'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
letter_list = string.ascii_letters + ' ' + '.'

name_html = soup.find('span', {'class':'b-content__title-highlight'})
stats = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})

name_rough = name_html.text
name = " ".join(name_rough.split())
#print(name)





stat_list = []
for stats in stats:
    info = stats.text
    better = " ".join(info.split())
    if better != '':
        stat_list.append(better)
#print(stat_list)
    
    
category_list = []
number_list = []    
for section in stat_list:
    temp_string_c = ''
    temp_string_n = ''
    trigger = False
    for letter in section:
        if trigger == False:
            if letter in letter_list:
                temp_string_c += letter
            if letter == ':':
                category_list.append(temp_string_c.strip())    
                trigger = True
        else:
            temp_string_n += letter
    number_list.append(temp_string_n.replace(',', '').strip())
#print(category_list)
#print(number_list)


display_dict_c = {}
display_dict_n = {}
filename = 'UFCtest.csv'
f= open(filename, 'w')


for i in range(len(stat_list)):
    display_dict_c[i] = category_list[i]
    display_dict_n[i] = number_list[i]
f.write('Name' + ',' + display_dict_c[0] + ',' + display_dict_c[1] + ',' + display_dict_c[2] + ',' + display_dict_c[3] + ',' + display_dict_c[4] + ',' + display_dict_c[5] + ',' + display_dict_c[6] + ',' + display_dict_c[7] + ',' + display_dict_c[8] + ',' + display_dict_c[9] + ',' + display_dict_c[10] + ',' + display_dict_c[11] + ',' + display_dict_c[12] + '\n') 
f.write(name + ',' + display_dict_n[0] + ',' + display_dict_n[1] + ',' + display_dict_n[2] + ',' + display_dict_n[3] + ',' + display_dict_n[4] + ',' + display_dict_n[5] + ',' + display_dict_n[6] + ',' + display_dict_n[7] + ',' + display_dict_n[8] + ',' + display_dict_n[9] + ',' + display_dict_n[10] + ',' + display_dict_n[11] + ',' + display_dict_n[12] + '\n') 

f.close()


