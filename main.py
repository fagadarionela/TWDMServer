import PIL.Image as pil
import flask
import os
import time
import torch
from flask import send_file

app = flask.Flask(__name__)

if (torch.cuda.is_available()):
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


@app.route('/', methods=['POST'])
def handle_request():
    files_ids = list(flask.request.files)
    imagefile = flask.request.files[files_ids[0]]

    with torch.no_grad():
        default_image = pil.open(imagefile).convert('L')

        name_dest_im = os.path.join("assets", "{}.jpeg".format("result"))
        default_image.save(name_dest_im)

        return send_file("assets\\result.jpeg", mimetype='image/jpeg')

app.run(host="0.0.0.0", port=5000, debug=False)
