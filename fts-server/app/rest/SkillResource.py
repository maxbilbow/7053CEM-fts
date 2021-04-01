from flask import jsonify
from flask_api import status
from injector import inject

from app.flask_app import app
from app.service.SkillService import SkillService


@inject
@app.route("/api/skill-list", methods=['GET'])
def get_skills(service: SkillService):
    return jsonify(service.get_all()), status.HTTP_200_OK
