import requests
from flask import current_app

def send_telegram_message(text):
    token = current_app.config.get("BOT_TOKEN")
    chat_id = current_app.config.get("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    return response.status_code == 200
import requests
from flask import current_app

def send_pdf_to_telegram(file_path):
    token = current_app.config.get("BOT_TOKEN")
    chat_id = current_app.config.get("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    with open(file_path, "rb") as doc:
        response = requests.post(url, data={"chat_id": chat_id}, files={"document": doc})
    return response.status_code == 200