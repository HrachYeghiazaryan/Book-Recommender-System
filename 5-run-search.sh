export EMBEDDINGS_DIR_NAME=zangak_embeddings_pq
export NUM_SIMILARS=10

python src/search.py \
-embeddings_dir_name=$EMBEDDINGS_DIR_NAME \
-num_similars=$NUM_SIMILARS