import argparse
import os
import shutil
import pandas as pd
import datetime
import yaml
import logging
from googletrans import Translator


#### Setting up argparse ####
parser = argparse.ArgumentParser()
parser.add_argument('-matched_data_dir_name', type=str, help='the name of the directory containing matched dataframe')
parser.add_argument('-translated_data_dir_name', type=str, help='the name of the directory to save the results of the translation')
args = parser.parse_args()

#### Defining directories ####
matched_data_path = f'data/book_text_matched/{args.matched_data_dir_name}/dataframe.csv'

current_dir = os.getcwd()

translated_data_dir = f'data/translated/{args.translated_data_dir_name}'
translated_df_path = f'{translated_data_dir}/dataframe.csv'
config_path = f'{translated_data_dir}/config.yaml'
log_path = f'{translated_data_dir}/log.txt'

#### Making the directory ####
if os.path.exists(translated_data_dir):
    shutil.rmtree(translated_data_dir)
os.makedirs(translated_data_dir)

#### Setting up logging ####
logging.basicConfig(filename=log_path, level=logging.INFO)

#### Reading the matched dataframe ####
df_matched = pd.read_csv(matched_data_path)

#### Main operations ####
translator = Translator()
df_vals = df_matched.values

translated_list = []
for i in range(len(df_vals)):
    try:
        translated_text = translator.translate(df_vals[i][3]).text
        translated_list.append([df_vals[i][0], df_vals[i][1], df_vals[i][2], df_vals[i][3], translated_text])
    except:
        print(f'The book "{df_vals[i][1]}" had error when translating. Skipping the book')
        logging.info(f'The book "{df_vals[i][1]}" had error when translating. Skipping the book')

df_translated = pd.DataFrame(translated_list, columns=['index','name','link', 'orig_text', 'trans_text'])

df_translated.to_csv(translated_df_path, index=False)

#### Saving the data of the experiment
cur_time = datetime.datetime.now().replace(microsecond=0).strftime('%d-%B-%Y %H:%M')
confdict = {'created_on': cur_time,
            'matched_data': args.matched_data_dir_name,
            'save_dir': args.translated_data_dir_name}

with open(config_path, 'w') as f:
    configs = yaml.dump(confdict, f)

shutil.copyfile(f'{current_dir}/src/translate.py', f'{translated_data_dir}/code.py')