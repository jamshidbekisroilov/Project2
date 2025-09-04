from flask import Blueprint, render_template, request
import requests
import os

news_bp = Blueprint('news', __name__, template_folder='templates')

@news_bp.route('/', methods=['GET', 'POST'])
def news_home():
    articles = []
    if request.method == 'POST':
        topic = request.form.get('topic')
        api_key = os.getenv('NEWS_API_KEY')
        url = f"https://newsapi.org/v2/everything?q={topic}&language=en&pageSize=5&apiKey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
    return render_template('news.html', articles=articles)
