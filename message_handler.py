# message_handler.py
import requests
from config import USER_ACCESS_TOKEN, API_URL

def handle_message(data):

    if "messages" in data.get("entry", [])[0].get("changes", [])[0].get("value", {}):
        # Extraer el mensaje
        message = data['entry'][0]['changes'][0]['value']['messages'][0]
        sender_id = message['from']
        
        # Identificar el tipo de mensaje
        if "text" in message:
            text = message['text']['body']
            print(f"Mensaje de texto recibido de {sender_id}: {text}")
            send_message(sender_id, f"Recibí tu mensaje de texto: {text}")
        
        elif "image" in message:
            image_id = message['image']['id']
            print(f"Imagen recibida de {sender_id}, ID: {image_id}")
            send_message(sender_id, "Recibí tu imagen. ¡Gracias!")
        
        elif "audio" in message:
            audio_id = message['audio']['id']
            print(f"Audio recibido de {sender_id}, ID: {audio_id}")
            send_message(sender_id, "Recibí tu audio. ¡Gracias!")
        
        elif "video" in message:
            video_id = message['video']['id']
            print(f"Video recibido de {sender_id}, ID: {video_id}")
            send_message(sender_id, "Recibí tu video. ¡Gracias!")
        
        elif "sticker" in message:
            sticker_id = message['sticker']['id']
            print(f"Sticker recibido de {sender_id}, ID: {sticker_id}")
            send_message(sender_id, "Recibí tu sticker. ¡Gracias!")
        
        else:
            print(f"Tipo de mensaje no reconocido de {sender_id}.")
            send_message(sender_id, "Recibí tu mensaje, pero no estoy seguro de qué tipo es.")


def send_message(recipient_id, message_text):

    try:

        headers = {
        "Authorization": f"Bearer {USER_ACCESS_TOKEN}",
        "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": recipient_id,
            "text": {"body": message_text}
        }
        # print(f"API_URL: {API_URL}")
        # print(f"Headers: {headers}")
        # print(f"Payload: {data}")
        response = requests.post(API_URL, json=data, headers=headers)
        # print(f"Response status code: {response.status_code}")
        # print(f"Response text: {response.text}")
        if response.status_code == 200:
            print("Mensaje enviado correctamente")
        else:
            print(f"Error al enviar el mensaje: {response.status_code}, {response.text}")

    except Exception as e:
        return e, 403

# Tipos de mensaje que se reciben
# Texto: El mensaje tendrá el campo "text".
# Imagen: El mensaje tendrá el campo "image".
# Audio: El mensaje tendrá el campo "audio".
# Video: El mensaje tendrá el campo "video".
# Sticker: El mensaje tendrá el campo "sticker".
# validar cuando si va a recibir pdf, docs, excel et...  