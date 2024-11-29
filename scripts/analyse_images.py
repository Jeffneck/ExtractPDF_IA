# analyze_images.py

import os
from utils.ai_utils import send_image_to_ai

def analyze_images(images_folder, json_output_folder):
    if not os.path.exists(json_output_folder):
        os.makedirs(json_output_folder)

    for image_file in os.listdir(images_folder):
        if image_file.endswith('.png'):
            image_path = os.path.join(images_folder, image_file)
            response = send_image_to_ai(image_path)
            output_file = os.path.join(json_output_folder, f"{os.path.splitext(image_file)[0]}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(response)
            print(f"Analyse de {image_file} terminée.")

if __name__ == "__main__":
    images_folder = './data/images/'
    json_output_folder = './data/json/'
    analyze_images(images_folder, json_output_folder)
