from flask import Flask, render_template, request


app = Flask(__name__)

GOPRO_NAME = 'cyclops1'
GOPRO_URL = 'http://10.5.5.9:8080/videos/DCIM/100GOPRO/'
SAVE_DIR = '/Users/wallacdc/Desktop/PhotoBooth/images/'


@app.route('/booth', methods=['GET','POST'])
def booth():
    if request.method == 'GET':

        return render_template(
            'booth.html'
        )

    elif request.method == 'POST':
        from settings import BOOTH
        BOOTH.take_photo()

        return render_template(
            'booth.html'
        )

if __name__ == '__main__':
    app.run(debug=True)
