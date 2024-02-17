#!/usr/bin/env python3
'''
    Use Babel to get user locale.
'''
from flask_babel import Babel, _
from flask import Flask, render_template, request, g
from typing import Union, Dict


app = Flask(__name__, template_folder="templates")
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''
    The `Config` class defines language settings and default locale
    and timezone for a Python application.
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user(id: int) -> Union[Dict[str, Union[str, None]], None]:
    """
    The function `get_user` retrieves a user's information based on
    their ID from a dictionary of users.
    """
    return users.get(int(id), None)


@app.before_request
def before_request() -> None:
    """
    `before_request` sets the `user` attribute in the global `g`
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


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
    if g.user:
        return g.user.get('locale', None)

    return request.accept_languages.best_match(app.config['LANGUAGES'])
# babel.init_app(app, locale_selector=get_locale)


@app.route('/', methods=['GET'], strict_slashes=False)
def helloworld() -> str:
    """
    The function `helloworld` returns the rendered
    template '1-index.html'.
    """
    return render_template('5-index.html', g=g)


if __name__ == '__main__':
    app.run()
