#!/usr/bin/env python3
"""
4. Force locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
import typing

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for available languages."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the best language match."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
