from flask import Flask, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

supported_locales = ['en', 'fr']

def get_user():
    login_as = request.args.get('login_as')
    if login_as and login_as.isdigit():
        return users.get(int(login_as))
    return None

@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale in supported_locales:
        return locale

    # 2. Locale from logged-in user
    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in supported_locales:
            return user_locale

    # 3. Locale from request headers
    best_match = request.accept_languages.best_match(supported_locales)
    if best_match:
        return best_match

    # 4. Default locale
    return 'en'
