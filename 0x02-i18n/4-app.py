#!/usr/bin/env python3
'''
    Use Babel to get user locale.
'''

from flask_babel import Babel, _
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


@babel.localeselector
def get_locale() -> str:
    """
    The function `get_locale()` returns the best matching
    language based on the accepted languages and
    the configured languages in the application.
    """
    my_locale = request.args.get('locale')
    if my_locale in app.config['LANGUAGES']:
        return my_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
# babel.init_app(app, locale_selector=get_locale)


@app.route('/', methods=['GET'], strict_slashes=False)
def helloworld() -> str:
    """
    The function `helloworld` returns the rendered
    template '1-index.html'.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
