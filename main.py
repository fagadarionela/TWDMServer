import os

import PIL.Image as image
import flask
from flask import send_file

app = flask.Flask(__name__)


# map the endpoint /
@app.route('/', methods=['POST'])
def handle_request():
    # the list of files sent by the client
    files_ids = list(flask.request.files)
    # get the image sent by the client
    imagefile = flask.request.files[files_ids[0]]

    # open the image and convert it greyscale
    default_image = image.open(imagefile).convert('L')

    # construct the path and then save the processed image
    current_path = os.path.dirname(__file__)  # Where main.py file is located
    assets_path = os.path.join(current_path, 'assets')  # The assets folder path
    name_dest_im = os.path.join(assets_path, "{}.jpeg".format("result"))
    default_image.save(name_dest_im)

    # send the response to the client
    return send_file("assets\\result.jpeg", mimetype='image/jpeg')


# run the app on your local ipv4 address on port 5000
app.run(host="0.0.0.0", port=5000, debug=False)
