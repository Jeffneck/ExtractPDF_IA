# main.py

import argparse
from scripts import create_images, analyze_images, transform_data

def main():
    parser = argparse.ArgumentParser(description='Outil de traitement PDF vers CSV.')
    parser.add_argument('--create-images', action='store_true', help='Créer les images à partir des PDFs.')
    parser.add_argument('--analyze-images', action='store_true', help='Analyser les images avec l\'IA et créer les JSON.')
    parser.add_argument('--transform-data', action='store_true', help='Concaténer les JSON et les transformer en CSV.')
    
    args = parser.parse_args()
    
    if args.create_images:
        create_images.create_images('./data/input_pdfs/', './data/split_pdfs/', './data/images/')
    elif args.analyze_images:
        analyze_images.analyze_images('./data/images/', './data/json/')
    elif args.transform_data:
        transform_data.transform_data('./data/json/', './data/output/combined_data.json', './data/output/output.csv')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
