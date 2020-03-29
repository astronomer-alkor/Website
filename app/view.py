from flask import (
    render_template
)

from .application import APP


@APP.route('/')
def index():
    return render_template('index.html')


@APP.errorhandler(404)
def page_not_found(_):
    return render_template('404.html'), 404
