from app.database.mongo import Database
from app.config import app
from injector import inject
import os
from flask_api import status
import time


@inject
@app.route("/test/db/add/<poi_id>", methods=['GET'])
def add_to_db(database: Database, poi_id: str):
    if os.environ.get('FLASK_ENV') != 'development':
        return "NOT ALLOWED", status.HTTP_403_FORBIDDEN

    print("inserting %s" % poi_id)
    try:
        res = database.update("poi_score", {
            "_id": poi_id,
            "id": poi_id,
            "updated": int(round(time.time() * 1000)),
            "score": 1,
            "numberOfReviews": 42,
            "factors": {
                "faceCoverings": 0,
                "socialDistancing": 0,
                "hygiene": 0
            }
        })
        print(res)
        return "OK"
    except Exception as e:
        print("FAIL")
        return str(e)
