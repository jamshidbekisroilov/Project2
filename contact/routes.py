from flask import Blueprint, render_template, request
import requests
import os

contact_bp = Blueprint('contact', __name__, template_folder='templates')

@contact_bp.route('/', methods=['GET', 'POST'])
def contact():
    status = None
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        telegram_token = os.getenv('BOT_TOKEN')
        telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        text = f"📩 New message from DevHub:\n👤 Name: {name}\n📝 Message: {message}"
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        payload = {
            'chat_id': telegram_chat_id,
            'text': text
        }
        response = requests.post(url, data=payload)
        status = "Message sent!" if response.status_code == 200 else "Failed to send."
    return render_template('contact.html', status=status)