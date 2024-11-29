# utils/csv_utils.py

import json
import csv

def json_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        if data:
            header = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=header, delimiter='\t')
            writer.writeheader()
            for item in data:
                writer.writerow(item)
    print(f"Données JSON écrites dans {output_file}.")
