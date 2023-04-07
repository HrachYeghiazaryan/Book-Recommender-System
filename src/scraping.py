import pandas as pd
import argparse
import logging
import os
import shutil
import yaml
import datetime
import time
import pickle

import requests
from bs4 import BeautifulSoup

#### Setting up argparse ####
parser = argparse.ArgumentParser()
parser.add_argument('-save_dir_name', type=str, help='the name of the directory to save the scraped data to')
parser.add_argument('-page_num', type=int, help='the number of pages to scrape')
args = parser.parse_args()

#### Defining directories ####
save_dir = f'data/raw_scraped/{args.save_dir_name}'
logging_path = f'{save_dir}/log.txt'
config_path = f'{save_dir}/config.yaml'

#### Making the directory ####
if os.path.exists(save_dir):
    shutil.rmtree(save_dir)
os.makedirs(save_dir)

#### Setting up logging ####
logging.basicConfig(filename=logging_path, level=logging.INFO)

#### Performing main operations ####
start = datetime.datetime.now().replace(microsecond=0)
print(f'scraping started at {start}')
logging.info(f'scraping started at {start}')

def scraper(url):
    response=requests.get(url)
    page=response.content
    page=BeautifulSoup(page,'html.parser') #changing the type to BeautifulSoup Object
    return page

names = []
links = []

for i in range(1, args.page_num+1):
    url=f'https://zangakbookstore.am/en/grqer?page={i}'
    try:
        page=scraper(url)
        h1_element = page.find_all("h1", class_="mb-3")
        h1_tags = h1_element

        for h1 in h1_tags:
            time.sleep(0.01)
            a_tag = h1.find('a')
            if a_tag:
                names.append(a_tag.text)
                links.append(a_tag['href'])
    except: 
        print('An error occured while scraping. Skipping the book.')
link_data = {'index': range(len(names)),'name': names, 'link': links}
df_link = pd.DataFrame(link_data)

texts = []
page_counter, present_pages = -1, []
for name in df_link.link:
    url = name
    page_counter += 1
    try:
        page_book=scraper(url)
        main=page_book.find_all('div', class_ = 'col-md-10')
        for div in main:
            text = div.text.strip()
            texts.append(text)
        present_pages.append(page_counter)
    except:
        print('An error occured while scraping. Skipping the book.')
text_data = {'index': present_pages, 'text': texts}

end = datetime.datetime.now().replace(microsecond=0) 
print(f'scraping ended at {end}')
logging.info(f'scraping ended at {end}')
print(f'the process of scraping took {end-start}')
logging.info(f'the process of scraping took {end-start}')

df_link.to_csv(f'{save_dir}/link_df.csv')
outfile = open(f'{save_dir}/text_dict.pkl', 'wb')
pickle.dump(text_data, outfile)
outfile.close()
#### Dumping a file with configs ####
cur_time = datetime.datetime.now().replace(microsecond=0).strftime('%d-%B-%Y %H:%M')
confdict = {'created_on': cur_time,
            'dir_name': args.save_dir_name,
            'num_pages': args.page_num}

with open(config_path, 'w') as f:
    configs = yaml.dump(confdict, f)