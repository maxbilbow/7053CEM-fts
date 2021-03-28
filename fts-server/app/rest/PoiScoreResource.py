# PoiScoreResource.py
from app.service.PoiScoreService import PoiScoreService
from app.database.mongo import Database
from app.config import app
from injector import inject
from flask import jsonify, request
from warnings import warn
from deprecated import deprecated

@inject
@app.route("/api/poi-list", methods=['POST'])
def get_poi_list(poi_score_service: PoiScoreService):
    req_data = request.get_json()["data"]
    id_list = req_data["attributes"]["idList"]
    poi_score_list = poi_score_service.get_poi_list(id_list)
    return jsonify({
        "data": {
            "id": req_data["id"],
            "type": req_data["type"],
            "attributes": {
                "poiScoreList": poi_score_list
            }
        }
    })

@inject
@app.route("/api/poi-detail/<poi_id>", methods=['GET'])
def get_poi(poi_score_service: PoiScoreService, poi_id: str):
    return jsonify(poi_score_service.get_poi_details(poi_id))


@deprecated(version="1.0.0", reason="Fails with many parameters. Use POST instead")
@inject
@app.route("/api/poi-list/<id_list_string>", methods=['GET'])
def get_poi_list_deprecated(poi_score_service: PoiScoreService, id_list_string: str):
    warn("Deprecated GET endpoint used for /poi-list")
    id_list = id_list_string.split(",")
    return jsonify(poi_score_service.get_poi_list(id_list))
