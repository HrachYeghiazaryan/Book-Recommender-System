export TRANSLATED_DATA_DIR_NAME=zangak_translated
export EMBEDDINGS_DIR_NAME=zangak_embeddings_pq

python src/embedding_extraction.py \
-translated_data_dir_name=$TRANSLATED_DATA_DIR_NAME \
-embeddings_dir_name=$EMBEDDINGS_DIR_NAME