import os
import json

def combine_json_files(input_folder, output_file):
    all_data = []

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                all_data.extend(data)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(all_data, outfile, ensure_ascii=False, indent=4)
    print(f"Tous les fichiers JSON ont été combinés dans {output_file}.")

if __name__ == "__main__":
    input_folder = './data/processed_json/'
    output_file = './data/final_output/combined_data.json'
    combine_json_files(input_folder, output_file)
