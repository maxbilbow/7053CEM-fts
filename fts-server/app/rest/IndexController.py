from flask import render_template, send_from_directory
from app.flask_app import app

# Serve React App
from app.rest.decorators import login_required


@app.route("/")
@app.route("/course-list")
@app.route("/course-info/<ignored>")
def home(ignored: str):
    return render_template('index.html')


@app.route("/user-profile")
@login_required
def authenticated_urls():
    return render_template('index.html')


@app.route("/manifest.json")
def manifest():
    return send_from_directory('../../build', 'manifest.json')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('../../build', 'favicon.ico')


@app.route('/robots.txt')
def robots():
    return send_from_directory('../../build', 'robots.txt')


@app.route('/service-worker.js')
def service_worker():
    return send_from_directory('../../build', 'service-worker.js')
