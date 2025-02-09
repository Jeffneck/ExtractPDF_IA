# Utiliser une image Python officielle (ici, version 3.12-slim)
FROM python:3.12-slim

# Installer les dépendances système nécessaires (exemple : poppler-utils pour pdf2image)
RUN apt-get update && apt-get install -y --no-install-recommends \
    poppler-utils \
 && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances et installer les modules Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier le reste de l’application dans le conteneur
COPY . .

# Définir le point d'entrée (vous pouvez passer des arguments via la commande Docker)
ENTRYPOINT ["python", "main.py"]
