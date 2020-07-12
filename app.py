import numpy as np
import pickle
#import matplotlib.pyplot as plt
import cv2
import base64
from flask import Flask, request, jsonify, render_template
app = Flask(__name__, template_folder='templates')
model = pickle.load(open('models/logistic_regression_model.pkl', 'rb'))

init_Base64 = 21;

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
        image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
        
        resized = cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)
        vect = np.asarray(resized, dtype="uint8")
        vect = vect.reshape(1, 1, 28, 28).astype('float32')

        my_prediction = model.predict(vect)
        

        return render_template('results.html', prediction = my_prediction)

if __name__ == '__main__':
    app.run(debug=True)


