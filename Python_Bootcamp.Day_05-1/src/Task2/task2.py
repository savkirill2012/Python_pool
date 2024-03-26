from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
from os import listdir
import mimetypes

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        cur_file = request.files['filename']
        mimetypes.init()
        try:
            if mimetypes.guess_type(cur_file.filename)[0]\
                        .split('/')[0] == 'audio':
                cur_file.save('music_files/'
                              f'{secure_filename(cur_file.filename)}')
                return redirect('/')
            else:
                return redirect('/error_type')
        except AttributeError:
            return redirect('/')
    elif request.method == 'GET':
        return render_template('main.html', files=listdir('music_files/'))


@app.route('/error_type', methods=['POST', 'GET'])
def error_type_page():
    if request.method == 'POST':
        return redirect('/')
    elif request.method == 'GET':
        return render_template('error_type.html')


if __name__ == '__main__':
    app.run(port=8888, debug=False)
