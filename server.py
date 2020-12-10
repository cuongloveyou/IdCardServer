import io
import os

from flask import Flask, request
from flask_cors import CORS, cross_origin

import numpy as np
import cv2
import base64

import matplotlib.pyplot as plt
from PIL import Image
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg

# Khởi tạo Flask Server Backend
app = Flask(__name__)

# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# http://127.0.0.1/add
# http://127.0.0.1/minus
# http://127.0.0.1/multi
# http://127.0.0.1/div


@app.route('/add', methods=['POST', 'GET'] )
@cross_origin(origin='*')
def add_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    kq = a + b
    return 'Kết quả là: ' + str(kq)


@app.route('/minus', methods=['POST','GET'] )
@cross_origin(origin='*')
def minus_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    kq = a - b
    return 'Kết quả là: ' + str(kq)


@app.route('/multi', methods=['POST','GET'] )
@cross_origin(origin='*')
def multi_process():
    return "Hàm nhân"


@app.route('/div', methods=['POST','GET'] )
@cross_origin(origin='*')
def div_process():
    return "Hàm chia"


@app.route('/viethoa', methods=['POST'] )
@cross_origin(origin='*')
def viethoa_process():
    s = request.form.get("chuoiinput")
    #s = request.args.get("chuoiinput")
    return s.upper()

@app.route('/', methods=['POST'] )
@cross_origin(origin='*')
def home_process():
    config = Cfg.load_config_from_name('vgg_transformer')
    config['weights'] = 'https://drive.google.com/uc?id=13327Y1tz1ohsm5YZMyXVMPIOjoOA0OaA'
    config['cnn']['pretrained'] = False
    config['device'] = 'cpu'
    config['predictor']['beamsearch'] = False
    detector = Predictor(config)
    imgbase64 = request.form.get("imgbase64")
    img = base64.b64decode(imgbase64)
    img = Image.open(io.BytesIO(img))
    s = detector.predict(img)
    return s

# Start Backend
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
    app.run(host='0.0.0.0', port=port)  # Start listening
    #app.run(host='127.0.0.1', port=port)  # Start listening