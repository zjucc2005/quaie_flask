# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from .config import config

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV') or 'default'])
db = SQLAlchemy(app)


@app.route('/')
def root():
    return 'Hello World!'
    # return render_template('errors/500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500
