import argparse
import pickle
import pandas as pd
import os
import shutil
import datetime
import yaml

#### Setting up argparse ####
parser = argparse.ArgumentParser()
parser.add_argument('-raw_data_dir_name', type=str, help='the name of the directory of scraped data')
parser.add_argument('-gap_index_list', type=str, help='the indices of books that the script did not manage to scrape text for')
parser.add_argument('-matched_data_dir_name', type=str, help='the name of the directory to save the matched data')
args = parser.parse_args()

#### Defining directories ####
raw_data_dir = f'data/raw_scraped/{args.raw_data_dir_name}'
text_dict_path = f'{raw_data_dir}/text_dict.pkl'
raw_df_path = f'{raw_data_dir}/link_df.csv'

current_dir = os.getcwd()

matched_data_dir = f'data/book_text_matched/{args.matched_data_dir_name}'
matched_df_path = f'{matched_data_dir}/dataframe.csv'
config_path = f'{matched_data_dir}/config.yaml'

#### Making the directory ####
if os.path.exists(matched_data_dir):
    shutil.rmtree(matched_data_dir)
os.makedirs(matched_data_dir)

#### Reading the data from raw scraping ####
infile = open(text_dict_path, 'rb')
dct = pickle.load(infile)
infile.close()

df = pd.read_csv(raw_df_path)[['index','name','link']]

#### Main operations ####
gap_ls = eval(args.gap_index_list)

df = df[~df['index'].isin(gap_ls)]
df['text'] = dct['text']

df.to_csv(matched_df_path, index=False)

#### Saving the data of the experiment
cur_time = datetime.datetime.now().replace(microsecond=0).strftime('%d-%B-%Y %H:%M')
confdict = {'created_on': cur_time,
            'raw_data': args.raw_data_dir_name,
            'gap_index_list': args.gap_index_list,
            'save_dir': args.matched_data_dir_name}

with open(config_path, 'w') as f:
    configs = yaml.dump(confdict, f)

shutil.copyfile(f'{current_dir}/src/book_text_match.py', f'{matched_data_dir}/code.py')