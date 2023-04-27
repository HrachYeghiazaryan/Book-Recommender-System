import argparse
import spacy
import numpy as np
import pandas as pd
import pyarrow
from googletrans import Translator

#### Setting up argparse ####
parser = argparse.ArgumentParser()
parser.add_argument('-embeddings_dir_name', type=str, help='the name of the directory to use embeddings from')
parser.add_argument('-num_similars', type=int, help='the number of most similar books to keep')
args = parser.parse_args()

#### Defining input text ####
text = ['samurai']

#### Defining translator ####
translator = Translator()

#### Defining the embedding extractor ####
nlp = spacy.load('en_core_web_md')

#### Main operations ####
text_vector = np.array([i.vector for i in nlp.pipe(text)][0])

df = pd.read_parquet(f'data/embeddings/{args.embeddings_dir_name}/dataframe.parquet', engine='pyarrow')
df['similarity_score'] = df['embedding'].apply(lambda x: np.sum(x*text_vector))
df = df.sort_values(by='similarity_score', ascending=False).head(args.num_similars)
print(df)