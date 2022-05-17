import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

with open(f'model2.pkl', "rb") as handle:
    model = pickle.load(handle)

flask_app = Flask(__name__)

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    # converting features
    columns = ['Loan amount', 'Family income', 'Loan term']
    values = pd.DataFrame([float_features], columns=columns)
    # features -> model
    prediction = model.predict(values).tolist()[0]
    if prediction == 0:
        mokumas = "mokus"
    else:
        mokumas = "nemokus"
    return render_template("index.html", prediction_text="Klientas yra : {}".format(mokumas))
    #, input_values=str(values)
@flask_app.route("/test")
def test_ok():
    return {"result": "ok"}

if __name__ == "__main__":
    flask_app.run(debug=True, port = 5001)