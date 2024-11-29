# create_images.py

import os
from utils.pdf_utils import split_pdf
from utils.image_utils import pdf_to_images

def create_images(input_pdf_folder, split_pdf_folder, images_folder):
    # Fractionner les PDFs
    for pdf_file in os.listdir(input_pdf_folder):
        if pdf_file.endswith('.pdf'):
            input_pdf_path = os.path.join(input_pdf_folder, pdf_file)
            split_pdf(input_pdf_path, split_pdf_folder)

    # Convertir les PDFs fractionnés en images
    for pdf_file in os.listdir(split_pdf_folder):
        if pdf_file.endswith('.pdf'):
            input_pdf_path = os.path.join(split_pdf_folder, pdf_file)
            pdf_to_images(input_pdf_path, images_folder)

if __name__ == "__main__":
    input_pdf_folder = './data/input_pdfs/'
    split_pdf_folder = './data/split_pdfs/'
    images_folder = './data/images/'
    create_images(input_pdf_folder, split_pdf_folder, images_folder)
