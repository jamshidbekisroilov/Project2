from flask import Blueprint, render_template, request, current_app
import requests
from utils.telegram import send_telegram_message

smart_recipes_bp = Blueprint('smart_recipes', __name__, template_folder='templates')

@smart_recipes_bp.route('/', methods=['GET', 'POST'])
def meal_plan():
    meals = []
    nutrients = {}

    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        api_key = current_app.config.get('SPOONACULAR_API_KEY')
        url = f"https://api.spoonacular.com/mealplanner/generate?timeFrame=day&apiKey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            meals = data.get('meals', [])
            nutrients = data.get('nutrients', {})

            # ✅ Telegramga yuborish shu yerda
            if meals:
                message = "🍽️ <b>Your Daily Meal Plan</b>\n\n"
                for meal in meals:
                    title = meal.get('title', 'No title')
                    ready = meal.get('readyInMinutes', '?')
                    servings = meal.get('servings', '?')
                    link = f"https://spoonacular.com/recipes/{title.replace(' ', '-')}-{meal.get('id', '')}"
                    message += f"• <b>{title}</b>\n⏱️ {ready} min | 🍽️ {servings} servings\n🔗 <a href='{link}'>View Recipe</a>\n\n"
                send_telegram_message(message)

    return render_template('smart_recipes.html', meals=meals, nutrients=nutrients)