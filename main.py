# -*- coding: utf-8 -*-
# This is a simple wrapper for running application
# $ python main.pyy
# $ gunicorn -w 4 -b 127.0.0.1:5000 main:app
# import os
# os.envrion['FLASK_ENV'] = 'production'
from app import app

if __name__ == '__main__':
    app.run(debug=True)
