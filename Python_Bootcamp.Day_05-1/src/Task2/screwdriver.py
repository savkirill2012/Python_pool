import argparse
import requests
from bs4 import BeautifulSoup

URL = 'http://localhost:8888/'


def pars_args() -> list[str, int]:
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', choices=['upload', 'list'], nargs=1)
    parser.add_argument("path", nargs='?')

    return parser.parse_args()


def upload_audio_file_to_server(name: str):
    with open(name, 'rb') as f:
        response = requests.post(URL, files={'filename': f})
        print(response)


def get_uploaded_audio_files():
    page = requests.get(URL).content
    soup = BeautifulSoup(page, "html.parser")
    ret_names = []
    for elem in soup.findAll('h1'):
        ret_names.append(str(elem)[4:-5])
    return ret_names


if __name__ == '__main__':
    args = pars_args()
    if args.cmd[0] == 'upload' and args.path:
        upload_audio_file_to_server(args.path)
    elif args.cmd[0] == 'list' and not args.path:
        print(get_uploaded_audio_files())
    else:
        raise ValueError('Invalid arguments')
