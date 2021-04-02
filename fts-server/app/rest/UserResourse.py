import logging

from flask import jsonify, request
from flask_api import status
from injector import inject

from app.flask_app import app
from app.rest.decorators import login_required
from app.rest.jsonapi.JsonApi import get_attributes, success_response, error_response
from app.service.UserService import UserService

logger = logging.getLogger("UserResource")

@inject
@app.route("/api/user-profile", methods=["GET"])
@login_required
def get_user_profile(service: UserService):
    """
    Returns profile as JSON structure
    """
    return jsonify(service.get_profile().to_dict()), status.HTTP_200_OK


@inject
@app.route("/api/user-profile", methods=["POST"])
@login_required
def update_user_profile(service: UserService):
    """
    Receives JSON API request containing a user profile object
    :returns JSON API response
    """
    profile, id, type = get_attributes("profile")
    try:
        logger.info("Updating profile with {}".format(profile))
        service.update_profile(profile)
        logger.info("Updating Seems to have worked")
        return success_response(id, type, dict()), status.HTTP_202_ACCEPTED
    except Exception as e:
        logger.exception(e)
        return error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR
