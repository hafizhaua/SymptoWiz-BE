from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import pickle
import json

def get_disease_info(name):
    disease_dict = json.load('disease.json')
    return disease_dict[name]

# def generate_df(symptoms):
#     pred_data = {}
#     for symptom_candidate in symptoms_list:
#         pred_data[symptom_candidate] = 1 if symptom_candidate in symptoms else 0

#     df = pd.DataFrame(pred_data, index=[""])
#     return df


app = Flask(__name__)
CORS(app, supports_credentials=True)
model = pickle.load(open("model.pkl", "rb"))

# @app.route("/api/prediction", methods=["POST", "GET"])
# @cross_origin(supports_credentials=True)
# def predict():
#     data = request.get_json(force=True)
#     x_pred = generate_df(data["symptoms"])
#     prediction = model.predict(x_pred)
#     output = prediction[0]
#     info = get_disease_info(output)
#     return jsonify(
#         {
#             "status": "success",
#             "data": {
#                 "name": output,
#                 "description": info["description"],
#                 "precautions": info["precautions"],
#                 "image": info["image"],
#                 "doctors": info["doctors"],
#                 "symptoms": info["symptoms"],
#             },
#         }
#     )

@app.route("/api/disease", methods=["POST", "GET"])
@cross_origin(supports_credentials=True)
def getData():
    data = request.get_json(force=True)
    disease = data["disease"]
    info = get_disease_info(disease)
    info["name"] = disease
    print(info)
    return jsonify({"status": "success", "data": info})


@app.route("/", methods=["GET"])
def index():
    return "Machine Learning Inference"


def custom_error(message, status_code):
    return make_response(jsonify(message), status_code)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
