export RAW_DATA_DIR_NAME=zangak_scrape
export GAP_INDEX_LIST=[11382,11999,12088,18375,18640]
export MATCHED_DATA_DIR_NAME=zangak_match

python src/book_text_match.py \
-raw_data_dir_name=$RAW_DATA_DIR_NAME \
-gap_index_list=$GAP_INDEX_LIST \
-matched_data_dir_name=$MATCHED_DATA_DIR_NAME