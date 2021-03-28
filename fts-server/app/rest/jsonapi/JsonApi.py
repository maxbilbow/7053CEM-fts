
def success_response(a_id: str, a_type: str, attributes: dict) -> dict:
    return {
        "data": {
            "id": a_id,
            "type": a_type,
            "attributes": attributes
        }
    }
