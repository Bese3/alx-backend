#!/usr/bin/env python3
'''
    Basic Babel setup.
'''
from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__, template_folder="templates")
babel = Babel(app)


class Config:
    '''
    The `Config` class defines language settings and default locale
    and timezone for a Python application.
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def helloworld() -> str:
    """
    The function `helloworld` returns the rendered
    template '1-index.html'.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
