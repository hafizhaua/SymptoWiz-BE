import numpy as np
import pandas as pd
from disease import get_disease_info, generate_df
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)
CORS(app, supports_credentials=True)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/api/prediction", methods=["POST", "GET"])
@cross_origin(supports_credentials=True)
def predict():
    # try:
    data = request.get_json(force=True)
    x_pred = generate_df(data["symptoms"])
    prediction = model.predict(x_pred)
    output = prediction[0]
    info = get_disease_info(output)
    return jsonify(
        {
            "status": "success",
            "data": {
                "name": output,
                "description": info["description"],
                "precautions": info["precautions"],
                "image": info["image"],
                "doctors": info["doctors"],
                "symptoms": info["symptoms"],
            },
        }
    )


# except:
#     return custom_error({"status": "error"}, 404)


@app.route("/api/disease", methods=["POST", "GET"])
@cross_origin(supports_credentials=True)
def getData():
    # try:
    data = request.get_json(force=True)
    disease = data["disease"]
    info = get_disease_info(disease)
    info["name"] = disease
    print(info)
    return jsonify({"status": "success", "data": info})


# except:
# return custom_error({"status": "error"}, 404)


@app.route("/", methods=["GET"])
def index():
    return "Machine Learning Inference"


def custom_error(message, status_code):
    return make_response(jsonify(message), status_code)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
