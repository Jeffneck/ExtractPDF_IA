import os
import base64
import requests
from config import API_KEY, PROMPT_FILE

def send_image_to_ai(image_path):
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    with open(PROMPT_FILE, 'r', encoding='utf-8') as prompt_file:
        prompt_text = prompt_file.read().strip()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": f"{prompt_text}\nImage base64:\n{image_base64}"}
        ],
        "max_tokens": 3000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()
    message_content = response_json['choices'][0]['message']['content']
    return message_content

def process_all_images():
    images_folder = './data/images/'
    output_folder = './data/ai_responses/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(images_folder):
        if filename.endswith('.png'):
            image_path = os.path.join(images_folder, filename)
            response = send_image_to_ai(image_path)
            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(response)
            print(f"Traitement de {filename} terminé.")

if __name__ == "__main__":
    process_all_images()
