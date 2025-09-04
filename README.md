# 🚀 DevHub — Smart Services in One Place

**DevHub** is a multifunctional web application built with Flask that combines three practical modules: a Recipe Finder, a News Aggregator, and a Job Listing platform. It also includes a Help section and a Contact form integrated with Telegram for real-time messaging.

---

## 📦 Features

- 🥣 **Recipe Finder** — Enter ingredients and get cooking ideas using Spoonacular API
- 📰 **News Aggregator** — Search for personalized news topics via NewsAPI
- 💼 **Job Listing** — Post and browse job offers, apply directly
- 📬 **Contact** — Send messages via email or Telegram bot
- 🧠 **Help** — Learn how each module works and how to use the platform
## 📬 Feedback & Contact

If you have suggestions, questions, or want to collaborate:

- Telegram: [@jamshidbekisroilov](https://t.me/jamshidbekisroilov)
- GitHub Issues: [project2](https://github.com/jamshidbekisroilov/project2)

---

## 📄 License

This project is open-source and available under the [MIT License]([LICENSE](https://github.com/jamshidbekisroilov/Project2/LICENSE)).
---

## 👨‍💻 WARNING!!! NOTE:
This project includes a planned feature to generate weekly meal plans in PDF format and deliver them to users via Telegram bot.
While the core logic is in place, this module is still under development and not yet finalized.
Contributions or feedback on this part are especially welcome.
---

## 👨‍💻 Author

**Jamshidbek Isroilov**  

Sales Economist | Aspiring Project Manager | Telegram Bot Developer  
[LinkedIn](https://linkedin.com/in/jamshidbek-isroilov) • [GitHub](https://github.com/jamshidbekisroilov) • [Website](https://jamshidbek.uz)

---

## 🛠 Technologies Used

- Python 3.10+
- Flask (modular blueprint architecture)
- Jinja2 (templating)
- HTML + CSS + Bootstrap
- Telegram Bot API
- Spoonacular API
- NewsAPI
- dotenv (for environment variables)

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/jamshidbekisroilov/devhub.git
cd devhub
pip install -r requirements.txt
create .env and werite enviroment variables
SPOONACULAR_API_KEY=your_spoonacular_api_key
NEWS_API_KEY=your_newsapi_key
BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=@your_channel_or_user_id
## Local testing
python app.py
