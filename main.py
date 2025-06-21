import http.server
import socketserver
from http import HTTPStatus
import sqlite3
from models.challenge import *
import urllib
import controllers.challenge
from common.handler import Handler

class MainHandler(Handler):
    def do_GET(self):
        controllers.challenge.create(self)
       
httpd = socketserver.TCPServer(('', 8000), MainHandler)
httpd.serve_forever()
