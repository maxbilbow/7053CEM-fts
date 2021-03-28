from injector import singleton, inject
from app.database.mongo import Database
import time
from app.service.AuthService import AuthService

TABLE = "poi_review"


@singleton
class PoiReviewRepository:
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_by_user_id(self, user_id: str) -> list:
        result = self.database.find_by_props(TABLE, {"userId": user_id})
        for review in result:
            del review["userId"] # Do not send this to the front end

    def insert(self, poi_review: dict) -> str:
        poi_review["timestamp"] = int(round(time.time() * 1000))
        poi_review["userId"] = AuthService.get_authenticated_user()["id"]
        return self.database.insert(TABLE, poi_review)

    def delete(self, review_id: str):
        return self.database.delete_by_id(TABLE, review_id)
