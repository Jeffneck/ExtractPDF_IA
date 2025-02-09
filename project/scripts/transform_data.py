# transform_data.py

import os
from .utils.json_utils import combine_json_files
from .utils.csv_utils import json_to_csv

def transform_data(json_folder, combined_json_path, output_csv_path):
    combine_json_files(json_folder, combined_json_path)
    json_to_csv(combined_json_path, output_csv_path)

if __name__ == "__main__":
    json_folder = './data/json/'
    combined_json_path = './data/output/combined_data.json'
    output_csv_path = './data/output/output.csv'
    transform_data(json_folder, combined_json_path, output_csv_path)
