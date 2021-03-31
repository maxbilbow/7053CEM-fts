from app.database.mongo import Database
from app.flask_app import app
from injector import inject
import os
from flask_api import status
import time

from app.repository.CourseRepository import CourseRepository


@inject
@app.route("/test/add-course/<title>", methods=['GET'])
def add_to_db(repo: CourseRepository, title: str):
    if os.environ.get('FLASK_ENV') != 'development':
        return "NOT ALLOWED", status.HTTP_403_FORBIDDEN

    print("inserting %s" % title)
    try:
        res = repo.update({
            "id": title.lower(),
            "updated": int(round(time.time() * 1000)),
            "title": title,
            "outcomes": ["A", "B", "C"],
            "prerequisites": [{"skillId": "D", "level": 1}]
        })
        print(res)
        return "OK"
    except Exception as e:
        print("FAIL")
        return str(e)
