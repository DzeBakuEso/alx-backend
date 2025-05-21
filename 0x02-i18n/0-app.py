#!/usr/bin/env python3
"""
Basic Flask application for internationalization project.

This module sets up a basic Flask app with a single route (`/`)
that renders a template with a welcome message.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Index route that renders the welcome page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
