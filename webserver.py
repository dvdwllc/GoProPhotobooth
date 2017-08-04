import os
import json

from flask import Flask, render_template, request


app = Flask(__name__, static_folder='templates/assets', static_url_path='/static')


@app.route('/booth', methods=['GET','POST'])
def booth():
    if request.method == 'GET':
        return render_template('booth.html')
    elif request.method == 'POST':
        from settings import BOOTH
        BOOTH.take_photo()
        BOOTH.get_photos_from_device()

        return render_template('booth.html')


@app.route('/slideshow', methods=['GET'])
def slideshow():
    return render_template('slideshow.html')


@app.route('/api/images', methods=['GET'])
def images():
    assets = os.listdir('templates/assets/')
    return json.dumps([file for file in assets if file.endswith('.jpg')])


if __name__ == '__main__':
    app.run(debug=True)
