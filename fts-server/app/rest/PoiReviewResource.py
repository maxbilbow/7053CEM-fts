# PoiReviewResource.py
from app.service.PoiReviewService import PoiReviewService
from app.config import app
from injector import inject
from flask import jsonify, request, session
import logging
from app.sdp_errors import InvalidRequestError
from flask_api import status
from app.rest.decorators import login_required_post, login_required

@inject
@app.route("/api/poi-review", methods=['GET'])
@login_required
def get_all_for_current_user(poi_review_service: PoiReviewService):
    return jsonify(poi_review_service.get_all_for_current_user()), status.HTTP_200_OK

@inject
@app.route("/api/poi-review", methods=['POST'])
@login_required_post
def set_poi_review(poi_review_service: PoiReviewService):
    req_data = request.get_json()["data"]
    logging.debug("")
    logging.debug("Incoming API request (/api/poi-review):")
    logging.debug(req_data)
    # ADDING REVIEW TO DB
    try:
        poi_review: dict = req_data["attributes"]["review"]
        review_id: str = poi_review_service.add_review(poi_review)
        logging.debug("Review saved!")
        return jsonify({
            "data": {
                "id": "review",
                "type": "submit",
                "attributes": {
                    "result": "success",
                    "review_id": review_id
                }
            }
        }), status.HTTP_201_CREATED

    except InvalidRequestError as e:
        logging.error("ERROR: Failed to post a review!")
        logging.error(e)

        return jsonify({
            "data": {
                "id": "review",
                "type": "submit",
                "attributes": {
                    "result": "fail",
                    "message": str(e)
                }
            }
        }), status.HTTP_400_BAD_REQUEST

    except Exception as e:
        logging.error("ERROR: Failed to post a review!")
        logging.error(e)

        return jsonify({
            "data": {
                "id": "review",
                "type": "submit",
                "attributes": {
                    "result": "fail",
                    "message": str(e)
                }
            }
        }), status.HTTP_500_INTERNAL_SERVER_ERROR
