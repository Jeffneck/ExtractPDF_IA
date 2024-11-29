import json
import csv

def json_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        if data:
            header = data[0].keys()
            writer.writerow(header)
            for item in data:
                row = [str(value).replace('.', ',') if isinstance(value, float) else value for value in item.values()]
                writer.writerow(row)
    print(f"Données JSON écrites dans {output_file}.")

if __name__ == "__main__":
    input_file = './data/final_output/combined_data.json'
    output_file = './data/final_output/output.csv'
    json_to_csv(input_file, output_file)
