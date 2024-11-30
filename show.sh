#!/bin/bash

# Vérifier si un argument est fourni
if [ $# -eq 0 ]; then
    echo "Usage: $0 <nom_du_fichier_sans_extension>"
    echo "Par exemple : ./show CDP_0050"
    exit 1
fi

FILENAME=$1

# Chemins vers les fichiers
IMAGE_PATH="./data/images/${FILENAME}.png"
JSON_PATH="./data/json/${FILENAME}.json"

# Vérifier si les fichiers existent et les ouvrir avec VSCode
if [ -f "$IMAGE_PATH" ]; then
    code "$IMAGE_PATH"
else
    echo "Le fichier image $IMAGE_PATH n'existe pas."
fi

if [ -f "$JSON_PATH" ]; then
    code "$JSON_PATH"
else
    echo "Le fichier JSON $JSON_PATH n'existe pas."
fi
