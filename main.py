from flask import Flask, request, redirect, url_for, flash, jsonify
from keras.models import load_model
import numpy as np

app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    model = load_model('ai-api/models/final_prediction')
    app.run(debug=True, host='0.0.0.0')
