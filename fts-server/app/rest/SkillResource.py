from flask import jsonify
from flask_api import status

from app.flask_app import app
from app.service.SkillService import SkillService


@app.route("/api/skill-list", methods=['GET'])
def get_skills(skill_service: SkillService):
    return jsonify(skill_service.get_all()), status.HTTP_200_OK
