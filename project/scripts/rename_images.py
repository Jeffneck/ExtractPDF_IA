# scripts/rename_images.py

import os

def rename_images(images_folder, prefix):
    if not os.path.exists(images_folder):
        print(f"Le dossier {images_folder} n'existe pas.")
        return

    images = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not images:
        print(f"Aucune image à renommer dans le dossier {images_folder}.")
        return

    images.sort()  # Tri pour assurer un ordre cohérent
    total_images = len(images)
    
    for idx, filename in enumerate(images, start=1):
        old_path = os.path.join(images_folder, filename)
        new_filename = f"{prefix}_{idx:04d}.png"
        new_path = os.path.join(images_folder, new_filename)
        
        # Vérifier si le nouveau nom de fichier existe déjà
        if os.path.exists(new_path):
            print(f"Le fichier {new_filename} existe déjà. Le renommage est interrompu.")
            return

        os.rename(old_path, new_path)
        print(f"Renommé : {filename} -> {new_filename}")
    
    print(f"Total de {total_images} images renommées avec le préfixe '{prefix}'.")

if __name__ == "__main__":
    images_folder = './data/images/'
    prefix = 'prefix'  # Remplacez par le préfixe souhaité
    rename_images(images_folder, prefix)
