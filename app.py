from flask import Flask, request, jsonify, render_template
import json
import base64
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('webcam.html')

@app.route('/download/',methods=['POST'])
def download():
    data = request.data
    jsonData = json.loads(data)
    pic = jsonData['picture']
    imgdata = base64.b64decode(pic)
    with open('img.png','wb') as f:
        f.write(imgdata)
    return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200), 200


if __name__ == '__main__':
    app.run()