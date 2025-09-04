from flask import Flask, render_template
from smart_recipes.routes import smart_recipes_bp
from news.routes import news_bp
from jobs.routes import jobs_bp
from contact.routes import contact_bp
from dotenv import load_dotenv
import os
from config import Config
load_dotenv()
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config.from_object(Config)
# Blueprintlarni ro‘yxatdan o‘tkazamiz
app.register_blueprint(smart_recipes_bp, url_prefix='/recipes')
app.register_blueprint(news_bp, url_prefix='/news')
app.register_blueprint(jobs_bp, url_prefix='/jobs')
app.register_blueprint(contact_bp, url_prefix='/contact')

# Home sahifasi
@app.route('/')
def home():
    return render_template('index.html')

# Help sahifasi
@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)