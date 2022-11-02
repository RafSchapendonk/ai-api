from flask import Flask, request, jsonify
from keras.models import load_model
import numpy as np
import os

app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    model = load_model('../models/final_prediction')
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=1, host="0.0.0.0", port=os.getenv("PORT") or 5000)
