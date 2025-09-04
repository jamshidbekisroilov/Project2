import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API keys
    SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
print("SPOONACULAR_API_KEY:", SPOONACULAR_API_KEY)
print("NEWS_API_KEY:", NEWS_API_KEY)
print("BOT_TOKEN:", BOT_TOKEN)
print("TELEGRAM_CHAT_ID:", TELEGRAM_CHAT_ID)