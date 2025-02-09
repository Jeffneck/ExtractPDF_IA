# utils/image_utils.py

from pdf2image import convert_from_path
import os
from datetime import datetime

def pdf_to_images(pdf_path, images_folder):
    # Obtenir la date actuelle au format AAAA_MM_JJ
    date = datetime.now().strftime("%Y_%m_%d")

    if not os.path.exists(images_folder):
        os.makedirs(images_folder)

    pages = convert_from_path(pdf_path, dpi=200)
    for i, page in enumerate(pages):
        output_path = os.path.join(images_folder, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{i+1}_{date}.png")
        page.save(output_path, 'PNG')
        print(f"Enregistré : {output_path}")
