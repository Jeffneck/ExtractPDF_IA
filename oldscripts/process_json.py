import os
import json
from datetime import datetime

def process_json_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            input_file_path = os.path.join(input_folder, filename)
            with open(input_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Ajoutez ici votre logique de traitement et de nettoyage des données
            for item in data:
                item['Date'] = datetime.now().strftime('%Y-%m-%d')
                item.setdefault('Entreprise', 'Votre Entreprise')
                item.setdefault('Disponibilité', 'OUI')
                # Ajoutez d'autres champs ou modifications nécessaires

            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Fichier {filename} traité.")

if __name__ == "__main__":
    input_folder = './data/ai_responses/'
    output_folder = './data/processed_json/'
    process_json_files(input_folder, output_folder)
