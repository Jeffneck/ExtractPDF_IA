# analyze_images.py

import os
import json
import re
from .utils.ai_utils import send_image_to_ai

def extract_json_from_response(response):
    """
    Extrait le contenu JSON de la réponse en supprimant les balises de code Markdown si elles sont présentes.
    """
    # Expression régulière pour détecter le code entre ```json et ```
    code_block_pattern = r'```(?:json)?\n([\s\S]*?)\n```'
    match = re.search(code_block_pattern, response, re.MULTILINE)
    if match:
        json_content = match.group(1)
    else:
        # Si aucune balise n'est trouvée, on suppose que la réponse est le contenu JSON
        json_content = response

    return json_content.strip()

def analyze_images(images_folder, json_output_folder, start_index=None, end_index=None):
    if not os.path.exists(json_output_folder):
        os.makedirs(json_output_folder)

    # Obtenir la liste des images
    images = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images.sort()  # Assurer un ordre cohérent

    # Si des indices sont fournis, filtrer les images
    if start_index is not None and end_index is not None:
        filtered_images = []
        for image_file in images:
            # Extraire l'indice de l'image à partir du nom du fichier
            match = re.search(r'_(\d+)\.png$', image_file)
            if match:
                index = int(match.group(1))
                if start_index <= index <= end_index:
                    filtered_images.append(image_file)
        images_to_analyze = filtered_images
    else:
        images_to_analyze = images

    for image_file in images_to_analyze:
        image_path = os.path.join(images_folder, image_file)
        response = send_image_to_ai(image_path)
        if response:
            cleaned_response = extract_json_from_response(response)

            # Tenter de parser le JSON pour s'assurer qu'il est valide
            try:
                json_data = json.loads(cleaned_response)
            except json.JSONDecodeError as e:
                print(f"Erreur lors du parsing du JSON pour le fichier {image_file}: {e}")
                print("Contenu de la réponse (non valide) :")
                print(cleaned_response)
                # Enregistrer le contenu non valide pour inspection
                error_file = os.path.join(json_output_folder, f"{os.path.splitext(image_file)[0]}_error.txt")
                with open(error_file, 'w', encoding='utf-8') as f:
                    f.write(response)
                continue  # Passer à l'image suivante

            # Ajouter le champ "Image" à chaque produit
            for item in json_data:
                item['Image'] = image_file  # ou utilisez image_path si vous voulez le chemin complet

            # Enregistrer le JSON modifié dans le fichier de sortie
            output_file = os.path.join(json_output_folder, f"{os.path.splitext(image_file)[0]}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)
            print(f"Analyse de {image_file} terminée.")
        else:
            print(f"Aucune réponse de l'API pour l'image {image_file}.")

if __name__ == "__main__":
    images_folder = './data/images/'
    json_output_folder = './data/json/'
    analyze_images(images_folder, json_output_folder)
