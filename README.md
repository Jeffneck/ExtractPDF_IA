Comment utiliser l'outil :
# Étape 1 : Créer les images
Lancez la commande suivante pour fractionner les PDFs et convertir les pages en images :

python main.py --create-images



# Étape 2 : Analyser les images et créer les JSON
Pour analyser les images avec le prompt IA et générer les fichiers JSON :

python main.py --analyze-images



# Étape 3 : Concaténer les JSON et transformer en CSV
Pour combiner tous les JSON en un seul fichier et le transformer en CSV :

python main.py --transform-data



Vous pouvez lancer chaque étape indépendamment selon vos besoins.