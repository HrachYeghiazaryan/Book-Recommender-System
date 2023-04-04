#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:01:47 2023

@author: anahithakobyan
"""
# book=page.find_all('section', class_ = 'mb-5')
# book=page.find_all('div', class_ = 'col-lg-8 col-xl-9')
# main=page.find_all('div', class_ = 'row no-gutters product-items-list items-list-container')
# main=page.find_all('div', class_ = 'col-6 col-md-4 col-lg-6 col-xl-4 col-xxl-3 mb-5 list-item')

import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

from pprint import pprint
import time

def scraper(url):
    response=requests.get(url)
    page=response.content
    page=BeautifulSoup(page,'html.parser') #changing the type to BeautifulSoup Object
    return page


names = []
links = []

#935
for i in range(1, 935):
    url=f'https://zangakbookstore.am/en/grqer?page={i}'
    page=scraper(url)
    h1_element = page.find_all("h1", class_="mb-3")
    h1_tags = h1_element

    for h1 in h1_tags:
        a_tag = h1.find('a')
        if a_tag:
            names.append(a_tag.text)
            links.append(a_tag['href'])
    

data = {'Name': names, 'Link': links}
df = pd.DataFrame(data)

#h1_element = page.find_all("h1", class_="mb-3")

# names = []
# links = []
# h1_tags = h1_element

# for h1 in h1_tags:
#     a_tag = h1.find('a')
#     if a_tag:
#         names.append(a_tag.text)
#         links.append(a_tag['href'])

# data = {'Name': names, 'Link': links}
# df = pd.DataFrame(data)

texts = []

for name in df.Link:
    url = name
    page_book=scraper(url)
    main=page_book.find_all('div', class_ = 'col-md-10')
    for div in main:
        text = div.text.strip()
        texts.append(text)


df['decription'] = texts
df.to_csv('Desktop/book_sample.csv')

# url_book = 'https://zangakbookstore.am/en/it-starts-with-us-1'
# page_book=scraper(url)
# main=page_book.find_all('div', class_ = 'col-md-10')
# for div in main:
#     text = div.text.strip()
#     print(text)


