# Import the Flask class. An instance of this class will be our WSGI application.
from flask import Flask
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def create_app():
    app = Flask(__name__)
    app.config.update(LIVESERVER_PORT=8847, TESTING=True)
    return app
