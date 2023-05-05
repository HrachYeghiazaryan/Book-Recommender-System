# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:19:19 2023

@author: Lenovo
"""
import argparse
import numpy as np
import pandas as pd
import spacy
from googletrans import Translator
import os
def perform_search(search_query, embeddings_dir_name, num_similars=5):
    #### Defining input text ####'
    parser = argparse.ArgumentParser()
    parser.add_argument('-embeddings_dir_name', type=str, default= r"zangak_embeddings_pq", help='the name of the directory to use embeddings from')
    parser.add_argument('-num_similars', type=int, default = 5, help='the number of most similar books to keep')
    args = parser.parse_args()
    text = [search_query]

    #### Defining translator ####
    translator = Translator()

    #### Defining the embedding extractor ####
    nlp = spacy.load('en_core_web_md')

    #### Main operations ####
    text_vector = np.array([i.vector for i in nlp.pipe(text)][0])

    df = pd.read_parquet(os.path.join('..','data', 'embeddings', args.embeddings_dir_name, 'dataframe.parquet'), engine='pyarrow')
    df['similarity_score'] = df['embedding'].apply(lambda x: np.sum(x*text_vector))
    df = df.sort_values(by='similarity_score', ascending=False).head(num_similars)

    search_results = []
    im_link='https://static.vecteezy.com/system/resources/previews/004/229/629/original/open-book-learn-free-vector.jpg'
    

    for i, row in df.reset_index(drop=True).iterrows(): # Reset the index to start from 0 and drop the old index
        description_limit = 150 
        name=f"{row['name']} --  "
        desc= row["orig_text"][:description_limit] + '  ...' if len(row["orig_text"]) > description_limit else row["orig_text"]
        link = row['link']     
        line = f"<div style='display: flex; align-items: center;'><div>\
                        <a href='{link}' style='color: #000000; text-decoration: none;'>\
                        <img src='{im_link}' alt='Image' width='90'></a>\
                        </div><div style='margin-left: 30px;'>\
                        <div style='font-weight: bold;'><a href='{link}' style='color: #000000; text-decoration: none;'>{name}</a></div>\
                        <div style='width: calc(100% - 100px); margin-left: 100px;'><div style='font-style: italic; font-weight: normal; color: #2F3036 ;'>{desc}</div>\
                        </div></div>"


        search_results.append(line)

    return search_results



