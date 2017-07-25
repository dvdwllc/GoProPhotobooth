from flask import Flask, render_template, request
from GoProPhotoBooth import GoProPhotoBooth

app = Flask(__name__)

Booth = GoProPhotoBooth('cyclops1',
                        'http://10.5.5.9:8080/videos/DCIM/100GOPRO/',
                        '/Users/wallacdc/Desktop/PhotoBooth/images/')

@app.route('/booth', methods=['GET','POST'])
def booth():
    if request.method == 'GET':

        return render_template(
            'booth.html'
        )

    elif request.method == 'POST':

        Booth.take_photo()

        return render_template(
            'booth.html'
        )

if __name__ == '__main__':
    app.run(debug=True)
