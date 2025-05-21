#!/usr/bin/env python3
from flask import Flask, request, g, render_template
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except Exception:
        return None

@app.before_request
def before_request():
    g.user = get_user()

@babel.timezoneselector
def get_timezone():
    # 1. Check URL parameter
    timezone = request.args.get("timezone")
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    # 2. Check user timezone
    if g.get("user"):
        user_tz = g.user.get("timezone")
        if user_tz:
            try:
                pytz.timezone(user_tz)
                return user_tz
            except UnknownTimeZoneError:
                pass

    # 3. Default timezone
    return "UTC"

@app.route('/')
def index():
    tz = get_timezone()
    user = g.get("user")
    return render_template('7-index.html', timezone=tz, user=user)

if __name__ == '__main__':
    app.run()
