#!/usr/bin/env python3
"""
5. Mock logging in
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict

app = Flask(__name__)
babel = Babel(app)


class Config:
    """App configuration for Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """Retrieve a user dictionary based on login_as URL param."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set user on flask.g before each request."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Select the best locale based on request or user settings."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the homepage with login message."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
