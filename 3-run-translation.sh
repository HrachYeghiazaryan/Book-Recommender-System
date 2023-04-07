export MATCHED_DATA_DIR_NAME=zangak_match
export TRANSLATED_DATA_DIR_NAME=zangak_translated

python src/translate.py \
-matched_data_dir_name=$MATCHED_DATA_DIR_NAME \
-translated_data_dir_name=$TRANSLATED_DATA_DIR_NAME