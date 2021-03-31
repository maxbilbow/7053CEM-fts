from flask import render_template, send_from_directory
from app.flask_app import app

# Serve React App
from app.rest.decorators import login_required


@app.route("/")
@app.route("/course-list")
def home():
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


@app.route('/logo192.png')
def logo192():
    return send_from_directory('../../build', 'logo192.png')


@app.route('/logo512.png')
def logo512():
    return send_from_directory('../../build', 'logo512.png')


@app.route('/robots.txt')
def robots():
    return send_from_directory('../../build', 'robots.txt')


@app.route('/service-worker.js')
def service_worker():
    return send_from_directory('../../build', 'service-worker.js')
