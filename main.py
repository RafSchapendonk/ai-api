import base64
import io

from flask import Flask, request, jsonify
from keras.models import load_model
# import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import os
# import shap

app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

# def plot_html():
#     data = request.get_json()
#     summary = shap.kmeans(X_test, 33)
#     prediction = np.array2string(model.predict(data))
#
#     explainer = shap.KernelExplainer(prediction, summary)
#     shap_values = explainer.shap_values(data)
#     shap.force_plot(explainer.expected_value, shap_values[0])
#
#     fig = plt.figure()
#
#     #
#     # summary = shap.kmeans(data.X_test, 50)
#     # e = shap.KernelExplainer(model.predict, summary)
#     # shap_values = e.shap_values(df_pred)
#     # shap.summary_plot(shap_values, df_pred, feature_names=df_pred.columns, show=None, plot_type='bar', max_display=10)
#     #
#
#     tmpfile = io.BytesIO()
#     fig.savefig(tmpfile, format='png')
#     encoded = base64.b64encode(tmpfile.getbuffer()).decode('ascii')
#     return f"<img src='data:image/png;base64,{encoded}' alt='Plot unable to load'/>"

if __name__ == '__main__':
    # X_test = pd.read_csv('./X_test.csv')
    model = load_model('models/final_prediction')
    app.run(debug=1, host="0.0.0.0", port=os.getenv("PORT") or 5000)

#     empty commit
