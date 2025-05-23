#!/usr/bin/env python3
"""Flask app with Babel and parametrized templates"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config for available languages and locale"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best language match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the localized template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
