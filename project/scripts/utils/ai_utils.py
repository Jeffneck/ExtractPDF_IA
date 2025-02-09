# utils/ai_utils.py

import base64
import requests
from config import API_KEY, PROMPT_FILE

def send_image_to_ai(image_path):
    # Encoder l'image en base64
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Lire le texte du prompt
    with open(PROMPT_FILE, 'r', encoding='utf-8') as prompt_file:
        prompt_text = prompt_file.read().strip()

    # Construire le message avec le nouveau format
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt_text
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": "gpt-4o-mini",  # Utilisez "gpt-4" si "gpt-4-vision" n'est pas disponible
        "messages": messages,
        "max_tokens": 3000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        response_json = response.json()
        message_content = response_json['choices'][0]['message']['content']
        return message_content
    else:
        # Gérer les erreurs de l'API
        print(f"Erreur {response.status_code}: {response.text}")
        return None
