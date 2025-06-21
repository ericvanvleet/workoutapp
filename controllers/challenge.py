from models.challenge import *
from common.errors import *
import http

def create(handler):
    try:
        challenge = Challenge(handler.get_parameter("start_date"), int(handler.get_parameter("day_count")), "Admin")
        #challenge.validate()
        handler.send_response(http.HTTPStatus.OK)
        handler.end_headers()
        handler.wfile.write(challenge.get_end_date().encode("utf-8"))

    except ChallengeValidationError as error:
        handler.send_response(http.HTTPStatus.BAD_REQUEST)
        handler.end_headers()
        handler.wfile.write(error.message.encode("utf-8"))

    except ValidationError as error:
        handler.send_response(http.HTTPStatus.BAD_REQUEST)
        handler.end_headers()
        handler.wfile.write(error.message.encode("utf-8"))