# scripts/test_prompt.py

import os
from .utils.ai_utils import send_image_to_ai
import json

def test_prompt(image_file, json_output_folder):
    if not os.path.exists(image_file):
        print(f"L'image {image_file} n'existe pas.")
        return

    if not os.path.exists(json_output_folder):
        os.makedirs(json_output_folder)

    response = send_image_to_ai(image_file)
    if response:
        # Enregistrer le JSON dans le dossier json_test
        output_file = os.path.join(json_output_folder, f"{os.path.splitext(os.path.basename(image_file))[0]}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response)
        print(f"Le JSON a été enregistré dans {output_file}.")

        # Afficher le JSON sur stdout
        print("Résultat JSON:")
        print(response)
    else:
        print("Aucune réponse de l'IA.")

if __name__ == "__main__":
    image_file = './path/to/your/image.png'
    json_output_folder = './data/json_test/'
    test_prompt(image_file, json_output_folder)
