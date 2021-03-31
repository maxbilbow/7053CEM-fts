import logging

from injector import inject

from app.database.MongoDB import MongoDb
from app.flask_app import app
from app.repository.TrainingEventRepository import TrainingEventRepository
from app.rest.decorators import dev_only


@inject
@app.route("/test/drop/<collection>", methods=['GET'])
@dev_only
def drop_all(collection: str):
    MongoDb()._db.drop_collection(collection)

    return "DONE"


@inject
@app.route("/test/add-course/<title>", methods=['GET'])
@dev_only
def add_to_db(repo: TrainingEventRepository, title: str):
    print("inserting %s" % title)
    try:
        te_dict = {
            "id": title.lower(),
            "title": title,
            "outcomes": ["A"],
            "prerequisites": ["A", "B", "c"]
        }
        res = repo._table.update(te_dict)
        print(res)
        return "OK"
    except Exception as e:
        print("FAIL")
        logging.exception(e)
        return str(e)
