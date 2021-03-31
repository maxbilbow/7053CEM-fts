# PoiReviewResource.py
from app.service.TrainingEventService import TrainingEventService
from app.flask_app import app
from injector import inject
from flask import jsonify

from flask_api import status
from app.rest.decorators import login_required

@inject
@app.route("/api/user-course-list", methods=['GET'])
@login_required
def get_all_for_current_user(course_service: TrainingEventService):
    return jsonify(course_service.get_all_for_current_user()), status.HTTP_200_OK

@inject
@app.route("/api/course-list", methods=['GET'])
def get_all(course_service: TrainingEventService):
    return jsonify(course_service.get_all()), status.HTTP_200_OK

