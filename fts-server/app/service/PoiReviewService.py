from injector import inject, singleton
from app.repository.PoiReviewRepository import PoiReviewRepository
from app.sdp_errors import InvalidRequestError
from app.service.PoiScoreService import PoiScoreService
from app.service.AuthService import AuthService
import logging

@singleton
class PoiReviewService:
    @inject
    def __init__(self, repository: PoiReviewRepository, poi_score_service: PoiScoreService):
        self.repository = repository
        self.poi_score_service = poi_score_service

    def get_all_for_current_user(self):
        user_id = AuthService.get_authenticated_user()["id"]
        return self.repository.get_by_user_id(user_id)

    def add_review(self, poi_review: dict) -> str:
        PoiReviewService.validate_review(poi_review)
        review_id = self.repository.insert(poi_review)
        logging.debug("Review saved with id: %s" % review_id)

        # Updated POI Score
        try:
            self.poi_score_service.update_with_review(poi_review)

        except Exception as e:
            logging.error("Failed to update score. Discarding review.")
            logging.error(e)
            try:
                self.repository.delete(review_id)
            except Exception as e1:
                logging.error("Failed to delete review")
                logging.error(e1)
            raise e

        return review_id

    @staticmethod
    def validate_review(poi_review: dict):
        if poi_review["score"] == 0:
            raise InvalidRequestError("Score should be -1 or 1")
        if poi_review["factors"] is None:
            raise InvalidRequestError("Factors not provided")
        factors = poi_review["factors"]
        if factors["faceCoverings"] is None:
            raise InvalidRequestError("faceCoverings factor not provided. Expected True or False")
        if factors["socialDistancing"] is None:
            raise InvalidRequestError("faceCoverings factor not provided. Expected True or False")
        if factors["hygiene"] is None:
            raise InvalidRequestError("faceCoverings factor not provided. Expected True or False")



