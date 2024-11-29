# utils/image_utils.py

from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, images_folder):
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)

    pages = convert_from_path(pdf_path, dpi=200)
    for i, page in enumerate(pages):
        output_path = os.path.join(images_folder, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{i+1}.png")
        page.save(output_path, 'PNG')
        print(f"Enregistré : {output_path}")
