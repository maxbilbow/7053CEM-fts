from injector import inject, singleton
from app.repository.PoiScoreRepository import PoiScoreRepository
import logging
from app.service.poi_score_utils import update_average, update_bool_average
from app.sdp_errors import InvalidRequestError


@singleton
class PoiScoreService:
    @inject
    def __init__(self, repository: PoiScoreRepository):
        self.repository = repository

    def get_poi_list(self, id_list: list) -> list:
        return self.repository.get_poi_with_ids(id_list)

    def get_poi_details(self, poi_id: str) -> dict:
        return self.repository.get_poi_details(poi_id)

    def update_with_review(self, poi_review: dict):
        poi_id = poi_review["poiId"]
        review_factors = poi_review["factors"]
        multiplier: int = poi_review["score"]
        poi_score = self.get_poi_details(poi_id)

        if multiplier != -1 and multiplier != 1:
            raise InvalidRequestError("Review score should be 1 or -1 but found %s" % multiplier)

        if poi_score is None:
            logging.debug("Creating new POI: %s: %s" % (poi_id, poi_review))
            self.repository.insert_or_update({
                "id": poi_id,
                "score": multiplier,
                "numberOfReviews": 1,
                "factors": {
                    "faceCoverings": multiplier * review_factors["faceCoverings"],
                    "socialDistancing": multiplier * review_factors["socialDistancing"],
                    "hygiene": multiplier * review_factors["hygiene"]
                }
            })
            return

        # Calculating new scores
        face_coverings = poi_score["factors"]["faceCoverings"]
        social_distancing = poi_score["factors"]["socialDistancing"]
        hygiene = poi_score["factors"]["hygiene"]

        logging.debug("Adding review to average for POI: %s" % poi_id)
        current_score = poi_score["score"]
        current_number_of_reviews = poi_score["numberOfReviews"]
        logging.debug("number of previous reviews: %s" % str(current_number_of_reviews))

        logging.debug("old score: " + str(current_score))
        new_score = update_average(current_score, current_number_of_reviews, multiplier)
        logging.debug("new score: " + str(new_score))

        logging.debug("old faceCoverings: " + str(face_coverings))
        new_face_coverings = update_bool_average(face_coverings, current_number_of_reviews,
                                                 review_factors["faceCoverings"], multiplier)
        logging.debug("new faceCoverings: " + str(new_face_coverings))

        logging.debug("old socialDistancing: " + str(social_distancing))
        new_social_distancing = update_bool_average(social_distancing,
                                                    current_number_of_reviews,
                                                    review_factors["socialDistancing"],
                                                    multiplier)
        logging.debug("new socialDistancing: " + str(new_social_distancing))

        logging.debug("old hygiene: " + str(hygiene))
        new_hygiene = update_bool_average(hygiene,
                                          current_number_of_reviews,
                                          review_factors["hygiene"],
                                          multiplier)
        logging.debug("new hygiene: " + str(new_hygiene))

        # Update POI scores with new, recalculated values
        poi_score["numberOfReviews"] += 1
        poi_score["score"] = new_score
        poi_score["factors"]["faceCoverings"] = new_face_coverings
        poi_score["factors"]["socialDistancing"] = new_social_distancing
        poi_score["factors"]["hygiene"] = new_hygiene
        return self.repository.insert_or_update(poi_score)
