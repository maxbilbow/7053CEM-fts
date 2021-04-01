import logging
from typing import Tuple, Any, Optional

from flask import request


def success_response(a_id: str, a_type: str, attributes: dict) -> dict:
    return {
        "data": {
            "id": a_id,
            "type": a_type,
            "attributes": attributes
        }
    }


def error_response(message: str):
    attrs, id, type = get_attributes()
    return {
        "data": {
            "id": id,
            "type": type,
            "errors": [message]
        }
    }


def get_attributes(attr: Optional[str] = None) -> Tuple[Any, str, str]:
    data: dict = request.get_json()["data"]
    attrs = data["attributes"]
    if attr is None:
        return attrs, data["id"], data["type"]
    else:
        return attrs[attr], data["id"], data["type"]
