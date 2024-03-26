from wsgiref.simple_server import make_server
from html import escape
from urllib.parse import parse_qs
import json


def application(environ, start_response):
    ret_dict = {'Cyberman': 'John Lumic',
                'Dalek': 'Davros',
                'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
                'Human': 'Leonardo da Vinci',
                'Ood': 'Klineman Halpen',
                'Silence': 'Tasha Lem',
                'Slitheen': 'Coca-Cola salesman',
                'Sontaran': 'General Staal',
                'Time Lord': 'Rassilon',
                'Weeping Angel': 'The Division Representative',
                'Zygon': 'Broton'}

    r = parse_qs(environ["QUERY_STRING"])
    response_body = {}
    status = '200 OK'
    arg = escape(r['species'][0])

    if arg in ret_dict.keys():
        response_body[arg] = ret_dict[arg]
    else:
        response_body[arg] = "Unknown"
        status = '404 Error'

    response_body = json.dumps(response_body) + '\n'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content_Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body.encode()]


if __name__ == '__main__':
    httpd = make_server('localhost', 8888, application)
    httpd.serve_forever()
