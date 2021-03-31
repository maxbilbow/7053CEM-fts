import logging

from app.database.mongo import Database
from app.flask_app import app
from injector import inject
import os
from flask_api import status
import time

from app.model.TrainingEvent import TrainingEvent
from app.repository.TrainingEventRepository import TrainingEventRepository


@inject
@app.route("/test/add-course/<title>", methods=['GET'])
def add_to_db(repo: TrainingEventRepository, title: str):
    if os.environ.get('FLASK_ENV') != 'development':
        return "NOT ALLOWED", status.HTTP_403_FORBIDDEN

    print("inserting %s" % title)
    try:
        te_dict = {
            "id": title.lower(),
            "title": title,
            "outcomes": [{"skillId": "D", "level": 2}],
            "prerequisites": [{"skillId": "D", "level": 1}]
        }
        res = repo._table.update(te_dict)
        print(res)
        return "OK"
    except Exception as e:
        print("FAIL")
        logging.exception(e)
        return str(e)
