#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:00:08 2021

@author: Jackson
"""



import requests
from bs4 import BeautifulSoup
import string
letter_list = string.ascii_letters + ' ' + '.'
number_string = '0123456789'

setup_url = 'http://ufcstats.com/fighter-details/1338e2c7480bdf9e'
#will change after initial setups


def write_categories(setup_url):
    '''
    input: Israel Adesanya url
        -arbitrary 
    output: writes stat categories
        -goes to top of excel sheet
        -one time use
        -returns None
    '''

    page = requests.get(setup_url)

    soup = BeautifulSoup(page.content, 'html.parser')

    stats = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})
    
    stat_list = []
    for stats in stats:
        info = stats.text
        better = " ".join(info.split())
        if better != '':
            stat_list.append(better)
            
    category_list = []    
    for section in stat_list:
        temp_string_c = ''
        for letter in section:
            if letter in letter_list:
                temp_string_c += letter
            if letter == ':':
                category_list.append(temp_string_c.strip())    
                break
                
    display_dict_c = {}
    filename = 'UFCcomp3.csv'
    f= open(filename, 'w')

    for i in range(len(stat_list)):
        display_dict_c[i] = category_list[i]
    f.write('Name' + ',' + display_dict_c[0] + ',' + display_dict_c[1] + ',' + display_dict_c[2] + ',' + display_dict_c[3] + ',' + display_dict_c[4] + ',' + display_dict_c[5] + ',' + display_dict_c[6] + ',' + display_dict_c[7] + ',' + display_dict_c[8] + ',' + display_dict_c[9] + ',' + display_dict_c[10] + ',' + display_dict_c[11] + ',' + display_dict_c[12] + '\n')

    f.close()
    
    return None

def get_name(URL):
    '''
    input: Url of specific fighter's stat page
        -from 
    output: fighter's name
        -goes to write_headers()
    '''
    #print(URL)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    name_html = soup.find('span', {'class':'b-content__title-highlight'})
   
    
    name_rough = name_html.text
    name = " ".join(name_rough.split())
    #print(name)
    return name
    




def get_stats(URL):
    '''
    input: Url of specific fighter's stat page
        -from
    output: list of fighter's stats (number_list)
        -goes to 
    '''
    
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    stats = soup.findAll('li', {'class':'b-list__box-list-item b-list__box-list-item_type_block'})
    
        
    stat_list = []
    for stats in stats:
        info = stats.text
        better = " ".join(info.split())
        if better != '':
            stat_list.append(better)
            
    number_list = []    
    for section in stat_list:
        temp_string_n = ''
        trigger = False
        for letter in section:
            if trigger == False:
                if letter == ':':    
                    trigger = True
            else:
                temp_string_n += letter
        number_list.append(temp_string_n.replace(',', '').strip())
    
    return number_list

def get_links(letter):
    '''
    input: letter of the alphabet
        -from loop
    output: list of links
        -goes to write_info()
    '''

    URL = 'http://ufcstats.com/statistics/fighters?char=' + letter + '&page=all'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    row = soup.findAll('tr', {'class':'b-statistics__table-row'})
    
    
    
    link_code_list = []
    for row in row:
        link_html = row.find('a')
        if link_html != None:
            trigger = False
            temp_string = ''
            counter = 0
            for letter in str(link_html):
                if trigger == False:
                    if letter == "/":
                        counter += 1 
                    if counter == 4:
                        temp_string += letter
                        trigger = True
                else:
                    if letter == '"':
                        break
                    else:
                        temp_string += letter
            link_code_list.append(temp_string)
            
    link_list = []
    for code in link_code_list:
        link_list.append('http://ufcstats.com/fighter-details' + code)
    
    return link_list    
    
def write_info(URL):
    display_dict_n = {}
    filename = 'UFCcomp3.csv'
    f= open(filename, 'w')
    name = get_name(URL)
    number_list = get_stats(URL)
    
    for i in range(len(number_list)):
        display_dict_n[i] = number_list[i]
    f.write(name + ',' + display_dict_n[0] + ',' + display_dict_n[1] + ',' + display_dict_n[2] + ',' + display_dict_n[3] + ',' + display_dict_n[4] + ',' + display_dict_n[5] + ',' + display_dict_n[6] + ',' + display_dict_n[7] + ',' + display_dict_n[8] + ',' + display_dict_n[9] + ',' + display_dict_n[10] + ',' + display_dict_n[11] + ',' + display_dict_n[12] + '\n') 

    f.close()


write_categories(setup_url) 
for letter in string.ascii_lowercase:
    link_list = get_links(letter)
    for URL in link_list:
        write_info(URL)

print("Done!")
  
    
    
    
    
    
    