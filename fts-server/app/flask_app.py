# Import the Flask class. An instance of this class will be our WSGI application.
from flask import Flask
import os
import logging, sys

app = Flask(__name__, static_folder="../build/static", template_folder="../build")
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

if (os.environ.get('FLASK_ENV') == 'development'):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
