#!/usr/bin/env python3
"""Flask app with Babel and locale selection from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for Babel settings"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Select the best match between supported languages
    and the 'Accept-Language' header from the request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders the homepage"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
