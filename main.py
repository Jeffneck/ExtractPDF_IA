# main.py

import argparse
from scripts import create_images, rename_images, analyze_images, transform_data, test_prompt

def main():
    parser = argparse.ArgumentParser(description='Outil de traitement PDF vers CSV.')
    parser.add_argument('--create-images', action='store_true', help='Créer les images à partir des PDFs.')
    parser.add_argument('--rename-images', type=str, help='Renommer les images avec le préfixe spécifié.')
    parser.add_argument('--analyze-images', nargs='*', help='Analyser les images avec l\'IA et créer les JSON.')
    parser.add_argument('--transform-data', action='store_true', help='Concaténer les JSON et les transformer en CSV.')
    parser.add_argument('--test-prompt', type=str, help='Tester le prompt IA avec une image spécifique.')

    args = parser.parse_args()

    if args.create_images:
        create_images.create_images('./data/input_pdfs/', './data/split_pdfs/', './data/images/')
    elif args.rename_images:
        rename_images.rename_images('./data/images/', args.rename_images)
    elif args.analyze_images is not None:
        # args.analyze_images est une liste des arguments fournis
        if len(args.analyze_images) == 0:
            # Pas d'indices fournis, analyser toutes les images
            analyze_images.analyze_images('./data/images/', './data/json/')
        elif len(args.analyze_images) == 2:
            # Deux indices fournis, analyser la plage spécifiée
            start_index = int(args.analyze_images[0])
            end_index = int(args.analyze_images[1])
            analyze_images.analyze_images('./data/images/', './data/json/', start_index, end_index)
        else:
            print("Veuillez fournir soit aucun indice, soit les indices de début et de fin pour --analyze-images.")
    elif args.transform_data:
        transform_data.transform_data('./data/json/', './data/output/combined_data.json', './data/output/output.csv')
    elif args.test_prompt:
        test_prompt.test_prompt(args.test_prompt, './data/json_test/')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
