import http
from common.errors import *

class Handler(http.server.SimpleHTTPRequestHandler):
    # def do_GET(self):
    #     controllers.challenge.create(self)
    def get_parameter(self, name):
        try:
            querystring = self.path[self.path.index("?") + 1:]
            parameters = urllib.parse.parse_qs(querystring)
        
        except ValueError as error:
            raise ValidationError(f'parameter {name} not found.')


        if not name in parameters:
            raise ValidationError(f'{name} is required.')
        if len(parameters[name]) != 1:
            raise ValidationError(f'more than 1 {name} found.')
        return parameters[name][0]