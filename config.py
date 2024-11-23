# config.py
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Variables principales
BUSINESS_ID = os.getenv("BUSINESS_ID")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")
USER_ACCESS_TOKEN = os.getenv("USER_ACCESS_TOKEN")
WABA_ID = os.getenv("WABA_ID")
VERSION = os.getenv("VERSION")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
# URL base de la API de WhatsApp
API_URL = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
