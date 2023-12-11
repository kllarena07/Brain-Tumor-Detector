from flask import Flask, request, jsonify
from flask_cors import CORS

from torch_utils import transform_image, get_prediction

app = Flask(__name__)
CORS(app)

import os
import io
import torch
from torchvision import transforms
from PIL import Image
from ultralytics import YOLO

model = YOLO('best.pt')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
      file = request.files.get('file')
      if file is None or file.filename == "":
        return jsonify({'error': 'no file'})
      if not allowed_file(file.filename):
        return jsonify({'error': 'format not supported'})

      buf = request.files["image_file"]
      results = model(buf)
      print(results)
    
    return jsonify({'result': 1})

if __name__ == "__main__":
  app.run(debug=True, port=8080)