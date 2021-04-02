from app.rest.jsonapi.JsonApi import success_response


class ResponseBuilder:
    @staticmethod
    def build_response(attributes: dict) -> dict:
        response = success_response("", "", attributes)
        return response

