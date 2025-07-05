import http.server
import socketserver
from http import HTTPStatus
import sqlite3
from models.challenge import *
import controllers.challenge
from common.handler import Handler

class MainHandler(Handler):
    def do_GET(self):
        path = self.path.split('?')[0]
        if path == '/create_challenge':
            controllers.challenge.create(self)
        elif path == '/list_challenges':
            controllers.challenge.list(self)
        else:
            self.not_found()
       
httpd = socketserver.TCPServer(('', 8000), MainHandler)
httpd.serve_forever()
