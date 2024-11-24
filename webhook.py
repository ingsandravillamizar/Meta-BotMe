# webhook.py
from flask import Flask, request, jsonify
from config import VERIFY_TOKEN

app = Flask(__name__)




@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verificación del webhook
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if token == VERIFY_TOKEN:
            return challenge, 200
        return "Token no válido", 403

    elif request.method == 'POST':
        # Procesar mensajes entrantes
        data = request.get_json()
        print("Mensaje recibido:", data)
        # Enviar a message_handler para procesar
        from message_handler import handle_message
        handle_message(data)
        return jsonify({"status": "received"}), 200
