from pdf2image import convert_from_path
import os

def pdf_to_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_pdf = os.path.join(input_folder, filename)
            pages = convert_from_path(input_pdf, dpi=200)
            for i, page in enumerate(pages):
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_{i+1}.png")
                page.save(output_path, 'PNG')
                print(f"Enregistré : {output_path}")

if __name__ == "__main__":
    input_folder = './data/input_pdfs/'
    output_folder = './data/images/'
    pdf_to_images(input_folder, output_folder)
