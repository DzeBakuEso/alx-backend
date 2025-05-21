from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
from pytz import timezone, UnknownTimeZoneError
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.before_request
def before_request():
    g.user = get_user()

def get_user():
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in ['en', 'fr']:
        return locale
    if g.user and g.user.get('locale') in ['en', 'fr']:
        return g.user.get('locale')
    return request.accept_languages.best_match(['en', 'fr'])

@babel.timezoneselector
def get_timezone():
    tz = request.args.get('timezone')
    if tz:
        try:
            timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass
    if g.user:
        user_tz = g.user.get('timezone')
        try:
            timezone(user_tz)
            return user_tz
        except UnknownTimeZoneError:
            pass
    return 'UTC'

@app.route('/')
def index():
    current_tz = get_timezone()
    now = datetime.now(timezone(current_tz))
    current_time = format_datetime(now)  # Uses default format & locale
    return render_template('index.html', current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)
