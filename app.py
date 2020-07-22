#import sys
#!{sys.executable} -m pip install opencv-python
#!{sys.executable} -m pip install Pillow
#!{sys.executable} -m pip install Flask

import numpy as np
#import pickle
#import matplotlib.pyplot as plt
import cv2
from PIL import Image
import base64
from flask import Flask, request, jsonify, render_template
app = Flask(__name__, template_folder='templates')


import tensorflow as tf
from tensorflow import keras
reconstructed_model = keras.models.load_model("models/sequential_nn_save.h5")

init_Base64 = 21;

np.set_printoptions(threshold = np.inf)

@app.route('/')
def home():
    return render_template('draw.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        draw = request.form['url']
        draw = draw[init_Base64:]
        draw_decoded = base64.b64decode(draw)
        image = np.asarray(bytearray(draw_decoded), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        image = image.sum(axis=2).astype(np.float32)
        resized = cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)
        vect = np.asarray(resized, dtype="uint8")
        vect = vect.reshape(1, 1, 1, 28*28).astype('float32')
        vect = vect[0][0]
        my_prediction = reconstructed_model.predict_classes(vect)
        confidence_vector = np.array(reconstructed_model.predict(vect))
        my_confidence = np.amax(confidence_vector)*100
        my_conclusion = 'I predict this digit is {} and I am {}% confident.'.format(my_prediction, my_confidence)

        return render_template('results.html', prediction = my_conclusion)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)


