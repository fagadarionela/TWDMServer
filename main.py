import flask
import os
import PIL.Image as pil

import torch
import time

from flask import send_file

app = flask.Flask(__name__)

if (torch.cuda.is_available()):
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


@app.route('/', methods=['POST'])
def handle_request():
    start_time1 = time.time()
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids), "\n")
    for file_id in files_ids:
        imagefile = flask.request.files[file_id]

        with torch.no_grad():
            default_image = pil.open(imagefile).convert('L')

            name_dest_im = os.path.join("assets", "{}_disp.jpeg".format("result"))
            default_image.save(name_dest_im)

            print("TIME: ")
            print(time.time() - start_time1)
            return send_file("assets\\result_disp.jpeg", mimetype='image/jpeg')
    print("\n")
    return "Image(s) Uploaded Successfully. Come Back Soon."


app.run(host="0.0.0.0", port=5000, debug=False)
