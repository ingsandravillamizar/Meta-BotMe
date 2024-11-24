# message_handler.py
import requests
from config import USER_ACCESS_TOKEN, API_URL

def handle_message(data):

    print (API_URL)
    if "messages" in data.get("entry", [])[0].get("changes", [])[0].get("value", {}):
        message = data['entry'][0]['changes'][0]['value']['messages'][0]
        sender_id = message['from']
        text = message.get('text', {}).get('body', '')

        print(f"Mensaje de {sender_id}: {text}")
        send_message(sender_id, f"Recibí tu mensaje: {text}")

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
