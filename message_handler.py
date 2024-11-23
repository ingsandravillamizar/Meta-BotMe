# message_handler.py
import requests
from config import API_URL, USER_ACCESS_TOKEN, RECIPIENT_PHONE_NUMBER

def send_message(recipient_id, message_text):
    headers = {
        "Authorization": f"Bearer {USER_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": recipient_id,
        "text": {"body": message_text}
    }
    response = requests.post(API_URL, json=data, headers=headers)
    if response.status_code == 200:
        print("Mensaje enviado correctamente")
    else:
        print(f"Error al enviar el mensaje: {response.status_code}, {response.text}")
