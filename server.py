from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
# import pickle
# import pandas as pd

symptoms_list = [
        "acidity",
        "back_pain",
        "bladder_discomfort",
        "breathlessness",
        "burning_micturition",
        "chest_pain",
        "chills",
        "constipation",
        "continuous_sneezing",
        "cough",
        "cramps",
        "fatigue",
        "headache",
        "high_fever",
        "indigestion",
        "joint_pain",
        "mood_swings",
        "muscle_wasting",
        "muscle_weakness",
        "neck_pain",
        "pain_during_bowel_movements",
        "patches_in_throat",
        "pus_filled_pimples",
        "shivering",
        "skin_rash",
        "stiff_neck",
        "stomach_pain",
        "sunken_eyes",
        "vomiting",
        "weakness_in_limbs",
        "weight_gain",
        "weight_loss",
        "yellowish_skin",
        "itching",
        "abdominal_pain",
        "anxiety",
        "blackheads",
        "blister",
        "bruising",
        "cold_hands_and_feets",
        "dehydration",
        "dizziness",
        "foul_smell_of urine",
        "knee_pain",
        "lethargy",
        "loss_of_appetite",
        "nausea",
        "nodal_skin_eruptions",
        "pain_in_anal_region",
        "restlessness",
        "skin_peeling",
        "sweating",
        "swelling_joints",
        "ulcers_on_tongue",
        "weakness_of_one_body_side",
        "altered_sensorium",
        "bloody_stool",
        "blurred_and_distorted_vision",
        "continuous_feel_of_urine",
        "dark_urine",
        "diarrhoea",
        "dischromic _patches",
        "extra_marital_contacts",
        "hip_joint_pain",
        "loss_of_balance",
        "movement_stiffness",
        "obesity",
        "red_sore_around_nose",
        "scurring",
        "silver_like_dusting",
        "spinning_movements",
        "swelling_of_stomach",
        "watering_from_eyes",
        "distention_of_abdomen",
        "excessive_hunger",
        "family_history",
        "irregular_sugar_level",
        "irritation_in_anus",
        "lack_of_concentration",
        "painful_walking",
        "passage_of_gases",
        "small_dents_in_nails",
        "spotting_ urination",
        "swollen_legs",
        "yellow_crust_ooze",
        "yellowing_of_eyes",
        "history_of_alcohol_consumption",
        "inflammatory_nails",
        "internal_itching",
        "mucoid_sputum",
        "swollen_blood_vessels",
        "unsteadiness",
        "depression",
        "fast_heart_rate",
        "fluid_overload",
        "malaise",
        "prominent_veins_on_calf",
        "puffy_face_and_eyes",
        "swelled_lymph_nodes",
        "enlarged_thyroid",
        "irritability",
        "mild_fever",
        "muscle_pain",
        "phlegm",
        "yellow_urine",
        "brittle_nails",
        "drying_and_tingling_lips",
        "increased_appetite",
        "visual_disturbances",
        "pain_behind_the_eyes",
        "polyuria",
        "slurred_speech",
        "swollen_extremeties",
        "throat_irritation",
        "toxic_look_(typhos)",
        "abnormal_menstruation",
        "acute_liver_failure",
        "belly_pain",
        "receiving_blood_transfusion",
        "red_spots_over_body",
        "redness_of_eyes",
        "rusty_sputum",
        "coma",
        "palpitations",
        "receiving_unsterile_injections",
        "sinus_pressure",
        "runny_nose",
        "stomach_bleeding",
        "congestion",
        "blood_in_sputum",
        "loss_of_smell"
    ]

# def generate_df(symptoms):
#     pred_data = {}
#     for symptom_candidate in symptoms_list:
#         pred_data[symptom_candidate] = 1 if symptom_candidate in symptoms else 0

#     df = pd.DataFrame(pred_data, index=[""])
#     return df

app = Flask(__name__)
CORS(app, supports_credentials=True)
# model = pickle.load(open("model.pkl", "rb"))

# @app.route("/api/prediction", methods=["POST", "GET"])
# @cross_origin(supports_credentials=True)
# def predict():
#     data = request.get_json(force=True)
#     x_pred = generate_df(data["symptoms"])
#     prediction = model.predict(x_pred)
#     output = prediction[0]
#     return jsonify({
#             "data": output
#         })


@app.route("/", methods=["GET"])
def index():
    return "Machine Learning Inference"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
