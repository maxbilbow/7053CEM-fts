# main.py
# Import the Flask class. An instance of this class will be our WSGI application.
from flask_injector import FlaskInjector
from app.dependencies import configure
from app.flask_app import app


# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
  app.run()
