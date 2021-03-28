from flask import render_template
from app.config import app

@app.route("/")
def index():
  return render_template("index.html")
