# utils/csv_utils.py

import json
import csv
from datetime import datetime

def json_to_csv(input_file, output_file):
    # Lire le contenu du fichier JSON
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Définir l'ordre souhaité des champs
    desired_order = [
        "Date",
        "Entreprise",
        "Ville",
        "Métier",
        "Code",
        "Catégorie",
        "Produit",
        "Marque Fournisseur",
        "Prix Kg",
        "Prix Litre",
        "Portionnement",
        "Prix portion",
        "Colisage",
        "Prix colis",
        "Disponibilité",
        "Surgelé",
        "Promotion",
        "Nouveauté",
        "Image"
    ]

    # Définir la correspondance entre les champs du JSON et les en-têtes du CSV
    field_mapping = {
        "Code": "Code",
        "Catégorie": "Catégorie",
        "Produit": "Produit",
        "Prix Kg": "Prix Kg",
        "Prix Litre": "Prix Litre",
        "Portionnement": "Portionnement",
        "Prix portion": "Prix portion",
        "Colisage": "Colisage",
        "Prix colis": "Prix colis",
        "Disponibilité": "Disponibilité",
        "Surgelé": "Surgelé",
        "Promotion": "Promotion",
        "Nouveauté": "Nouveauté",
        "Image": "Image"
    }

    # Traiter chaque élément du JSON
    processed_data = {}  # Utiliser un dictionnaire avec le code produit comme clé
    for item in data:
        # Créer un nouveau dictionnaire pour l'élément transformé
        new_item = {}

        # Ajouter les champs avec des valeurs par défaut
        new_item["Date"] = datetime.now().strftime('%Y-%m-%d')
        new_item["Entreprise"] = "Coup de pates"  # Vous pouvez modifier le nom de l'entreprise si nécessaire
        new_item["Ville"] = ""
        new_item["Métier"] = ""
        new_item["Marque Fournisseur"] = ""
        new_item["Disponibilité"] = ""
        new_item["Surgelé"] = ""
        new_item["Promotion"] = ""
        new_item["Nouveauté"] = ""

        # Copier et renommer les champs depuis l'item original
        for old_field, new_field in field_mapping.items():
            value = item.get(old_field, "")
            new_item[new_field] = value

        # Remplacer les points par des virgules dans les champs de prix
        price_fields = ["Prix au kg", "Prix au Litre", "Prix par portion", "Prix par colis"]
        for field in price_fields:
            if field in new_item and new_item[field]:
                # Convertir en chaîne et remplacer le point par une virgule
                new_item[field] = str(new_item[field]).replace('.', ',')
            else:
                new_item[field] = ""
        
        # Ajouter un préfixe au code produit
        code_field = "Code"
        if new_item.get(code_field, ""):
            # Ajouter le préfixe "CDP_"
            new_item[code_field] = "CDP_" + str(new_item[code_field])
        else:
            new_item[code_field] = ""

        # Vérifier si un élément avec le même code existe déjà
        code = new_item.get("Code", "")
        image = new_item.get("Image", "")
        if code:
            if code in processed_data:
                existing_item = processed_data[code]
                old_image = existing_item.get("Image", "")

                # Compter le nombre de champs non nuls pour le nouvel élément
                non_null_fields_new = sum(1 for v in new_item.values() if v not in ("", None, 0))

                # Compter le nombre de champs non nuls pour l'élément existant
                non_null_fields_existing = sum(1 for v in existing_item.values() if v not in ("", None, 0))

                if non_null_fields_new > non_null_fields_existing:
                    # Le nouvel élément a plus de champs non nuls, le remplacer
                    processed_data[code] = new_item
                    print(f"Img {image} -- Old Img {old_image} ---- L'élément avec le code {code} a été remplacé par un élément contenant moins de champs nuls.")
                else:
                    # Ne pas ajouter le nouvel élément
                    print(f"Img {image} -- Old Img {old_image} ---- L'élément avec le code {code} existe déjà avec moins de champs nuls. Ignoré.")
            else:
                # Ajouter le nouvel élément
                processed_data[code] = new_item
        else:
            # Si le code est vide, générer un code unique ou ignorer
            print(f"Img {image} ----- Aucun code produit disponible pour cet élément. Ignoré.")

    # Écrire les données dans un fichier TSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')

        # Écrire l'en-tête
        writer.writerow(desired_order)

        # Écrire chaque élément avec les champs dans l'ordre souhaité
        for item in processed_data.values():
            row = []
            for field in desired_order:
                value = item.get(field, "")
                row.append(value)
            writer.writerow(row)

    print(f"Données JSON écrites dans {output_file}.")
