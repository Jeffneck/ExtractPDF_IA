import PyPDF2
import os

def split_pdf(input_pdf, output_dir, pages_per_split=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_pdf, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        total_pages = len(reader.pages)

        for start_page in range(0, total_pages, pages_per_split):
            writer = PyPDF2.PdfWriter()
            end_page = min(start_page + pages_per_split, total_pages)

            for page_num in range(start_page, end_page):
                writer.add_page(reader.pages[page_num])

            output_pdf = os.path.join(output_dir, f"split_{(start_page // pages_per_split) + 1}.pdf")
            with open(output_pdf, 'wb') as outfile:
                writer.write(outfile)
            print(f"Créé : {output_pdf}")

if __name__ == "__main__":
    input_pdf = './data/input_pdfs/full_input.pdf'
    output_dir = './data/split_pdfs/'
    split_pdf(input_pdf, output_dir)
