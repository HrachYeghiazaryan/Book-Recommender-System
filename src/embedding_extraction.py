import argparse
import pandas as pd
import os
import shutil
import yaml
import datetime
import spacy


#### Setting up argparse ####
parser = argparse.ArgumentParser()
parser.add_argument('-translated_data_dir_name', type=str, help='the name of the directory containing translated dataframe')
parser.add_argument('-embeddings_dir_name', type=str, help='the name of the directory containing embeddings dataframe')
args = parser.parse_args()

#### Defining directories ####
translated_df_path = f'data/translated/{args.translated_data_dir_name}/dataframe.csv'

current_dir = os.getcwd()

embeddings_dir = f'data/embeddings/{args.embeddings_dir_name}'
embeddings_df_path = f'{embeddings_dir}/dataframe.csv'
config_path = f'{embeddings_dir}/config.yaml'

#### Making the directory ####
if os.path.exists(embeddings_dir):
    shutil.rmtree(embeddings_dir)
os.makedirs(embeddings_dir)

#### Reading the translated dataframe ####
df= pd.read_csv(translated_df_path).drop('index', axis=1)

#### Main operations ####
nlp = spacy.load('en_core_web_md')

text_vectors = []
for doc in nlp.pipe(df['trans_text']):
    text_vectors.append(doc.vector)
df['embedding'] = text_vectors

df = df[['name','link','orig_text','embedding']]

df.to_csv(embeddings_df_path, index=False)

#### Saving the data of the experiment
cur_time = datetime.datetime.now().replace(microsecond=0).strftime('%d-%B-%Y %H:%M')
confdict = {'created_on': cur_time,
            'translated_data': args.translated_data_dir_name,
            'save_dir': args.embeddings_dir_name}

with open(config_path, 'w') as f:
    configs = yaml.dump(confdict, f)

shutil.copyfile(f'{current_dir}/src/embedding_extraction.py', f'{embeddings_dir}/code.py')