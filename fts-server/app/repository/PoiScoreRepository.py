from injector import singleton, inject
from app.database.mongo import Database
import time

POI_SCORE_TABLE = "poi_score"


@singleton
class PoiScoreRepository:
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_poi_with_ids(self, id_list: list) -> list:
        return self.database.find_all_by_id(POI_SCORE_TABLE, id_list)

    def get_poi_details(self, poi_id: str) -> dict:
        return self.database.find_one_by_id(POI_SCORE_TABLE, poi_id)

    def insert_or_update(self, poi_score: dict):
        poi_score["updated"] = int(round(time.time() * 1000)),
        return self.database.update(POI_SCORE_TABLE, poi_score)
