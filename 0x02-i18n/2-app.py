#!/usr/bin/env python3
"""First you will setup a basic Flask app in 0-app.py
"""
from flask import Flask, render_template, request, localeselector
from flask_babel import Babel, Locale, timezone
from typing import Optional, Text

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale() -> Optional[Locale]:
    """get_locale"""
    return request.accept_languages.best_match(Config.BABEL_DEFAULT_LOCALE)


@app.route("/", strict_slashes=False)
def run() -> Text:
    """return templates/2-index.html"""
    return render_template("2-index.html", lang=Config.BABEL_DEFAULT_LOCALE)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
