from models.challenge import *
from common.errors import *
import http
from views.challenge_list import *
from pystache import Renderer
renderer = Renderer()

def create(handler):
    try:
        challenge = Challenge(None, handler.get_parameter("start_date"), int(handler.get_parameter("day_count")))
        challenge.save()
        # challenge.validate()
        handler.send_response(http.HTTPStatus.OK)
        handler.end_headers()
        handler.wfile.write(challenge.get_end_date().encode("utf-8"))
        # handler.wfile.write(handler.path.split('?')[0].encode("utf-8"))

    except ChallengeValidationError as error:
        handler.send_response(http.HTTPStatus.BAD_REQUEST)
        handler.end_headers()
        handler.wfile.write(error.message.encode("utf-8"))

    except ValidationError as error:
        handler.send_response(http.HTTPStatus.BAD_REQUEST)
        handler.end_headers()
        handler.wfile.write(error.message.encode("utf-8"))

def list(handler):
    challenges = Challenge.list()
    view = ChallengeList(challenges)
    handler.send_response(http.HTTPStatus.OK)
    handler.end_headers()
    handler.wfile.write(renderer.render(view).encode("utf-8"))