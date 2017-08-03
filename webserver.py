from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__, static_folder='templates/assets', static_url_path='/static')


@app.route('/booth', methods=['GET','POST'])
def booth():
    if request.method == 'GET':
        return render_template('booth.html')
    elif request.method == 'POST':
        from settings import BOOTH
        BOOTH.take_photo()

        return render_template('booth.html')


@app.route('/slideshow', methods=['GET'])
def slideshow():
    return render_template('slideshow.html')

if __name__ == '__main__':
    app.run(debug=True)
