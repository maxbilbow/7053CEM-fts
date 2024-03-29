# PoiReviewResource.py
from app.flask_app import app
from app.rest.decorators import login_required
from app.service.TrainingEventService import TrainingEventService
from flask import jsonify
from flask_api import status
from injector import inject


@inject
@app.route("/api/user-course-list", methods=['GET'])
@login_required
def get_all_for_current_user(course_service: TrainingEventService):
    return jsonify(course_service.get_all_for_current_user()), status.HTTP_200_OK

@inject
@app.route("/api/course-list", methods=['GET'])
def get_all(course_service: TrainingEventService):
    return jsonify(course_service.find_all_within_days()), status.HTTP_200_OK


@inject
@app.route("/api/course-info/<event_id>", methods=['GET'])
def get_training_event(course_service: TrainingEventService, event_id: str):
    return jsonify(course_service.find_by_id(event_id)), status.HTTP_200_OK

