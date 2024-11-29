import os
from send_to_ai import send_image_to_ai

def test_ai_prompt(image_files):
    for image_file in image_files:
        if os.path.exists(image_file):
            response = send_image_to_ai(image_file)
            print(f"Réponse de l'IA pour {image_file} :\n{response}")
        else:
            print(f"L'image {image_file} n'existe pas.")

if __name__ == "__main__":
    images_to_test = ['./data/images/sample_1.png']  # Spécifiez vos images ici
    test_ai_prompt(images_to_test)
