# Import the Flask class. An instance of this class will be our WSGI application.
from flask import Flask, render_template, send_from_directory
import os
import logging, sys

# Next we create an instance of this class. The first argument is the name of the application’s module or package.
# If you are using a single module (as in this example), you should use name because depending on if
# it’s started as application or imported as module the name will be different ('main' versus the actual import name).
# This is needed so that Flask knows where to look for templates, static files, and so on.
app = Flask(__name__, static_folder="../build/static", template_folder="../build")
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

if (os.environ.get('FLASK_ENV') == 'development'):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# Serve React App
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/manifest.json")
def manifest():
    return send_from_directory('../build', 'manifest.json')

@app.route('/favicon.ico')
def favicon():
  return send_from_directory('../build', 'favicon.ico')

@app.route('/logo192.png')
def logo192():
  return send_from_directory('../build', 'logo192.png')

@app.route('/logo512.png')
def logo512():
  return send_from_directory('../build', 'logo512.png')

@app.route('/robots.txt')
def robots():
  return send_from_directory('../build', 'robots.txt')
