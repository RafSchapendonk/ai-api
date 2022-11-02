from flask import Flask, request, redirect, url_for, flash, jsonify
from keras.models import load_model
import numpy as np

app = Flask(__name__)


@app.route('/')
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))


if __name__ == '__main__':
    model = load_model('../models/final_prediction')
    app.run(debug=True, host='0.0.0.0')
