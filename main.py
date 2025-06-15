import http.server
import socketserver
from http import HTTPStatus
import sqlite3
from challenge import *
import urllib

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

def get_parameter(path, name):
    querystring = path[path.index("?") + 1:]
    parameters = urllib.parse.parse_qs(querystring)
    if not name in parameters:
        raise ValidationError(f'{name} is required.')
    if len(parameters[name]) != 1:
        raise ValidationError(f'more than 1 {name} found.')
    return parameters[name][0]

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            challenge = Challenge(get_parameter(self.path, "start_date"), int(get_parameter(self.path, "day_count")), "Admin")
            #challenge.validate()
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(challenge.get_end_date().encode("utf-8"))

        except ChallengeValidationError as error:
            self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()
            self.wfile.write(error.message.encode("utf-8"))

        except ValidationError as error:
            self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()
            self.wfile.write(error.message.encode("utf-8"))


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()

