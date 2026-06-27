from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# -----------------------------
# Load Saved Files
# -----------------------------
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
encoders = joblib.load("models/encoder.pkl")

# Feature order (must match training)
FEATURE_COLUMNS = [
    "CODE_GENDER",
    "FLAG_OWN_CAR",
    "FLAG_OWN_REALTY",
    "CNT_CHILDREN",
    "AMT_INCOME_TOTAL",
    "NAME_INCOME_TYPE",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "NAME_HOUSING_TYPE",
    "DAYS_BIRTH",
    "DAYS_EMPLOYED",
    "FLAG_MOBIL",
    "FLAG_WORK_PHONE",
    "FLAG_PHONE",
    "FLAG_EMAIL",
    "OCCUPATION_TYPE",
    "CNT_FAM_MEMBERS"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {}

    categorical = [
        "CODE_GENDER",
        "FLAG_OWN_CAR",
        "FLAG_OWN_REALTY",
        "NAME_INCOME_TYPE",
        "NAME_EDUCATION_TYPE",
        "NAME_FAMILY_STATUS",
        "NAME_HOUSING_TYPE",
        "OCCUPATION_TYPE"
    ]

    # Encode categorical values
    for col in categorical:
        value = request.form.get(col)

        print(f"{col} -> {value}")

        data[col] = encoders[col].transform([value])[0]

    # Numerical values
    data["CNT_CHILDREN"] = float(request.form.get("CNT_CHILDREN") or 0)
    data["AMT_INCOME_TOTAL"] = float(request.form.get("AMT_INCOME_TOTAL") or 0)
    data["DAYS_BIRTH"] = float(request.form.get("DAYS_BIRTH") or 0)
    data["DAYS_EMPLOYED"] = float(request.form.get("DAYS_EMPLOYED") or 0)
    data["FLAG_MOBIL"] = float(request.form.get("FLAG_MOBIL") or 0)
    data["FLAG_WORK_PHONE"] = float(request.form.get("FLAG_WORK_PHONE") or 0)
    data["FLAG_PHONE"] = float(request.form.get("FLAG_PHONE") or 0)
    data["FLAG_EMAIL"] = float(request.form.get("FLAG_EMAIL") or 0)
    data["CNT_FAM_MEMBERS"] = float(request.form.get("CNT_FAM_MEMBERS") or 1)

    # Create DataFrame in correct order
    input_df = pd.DataFrame([[data[col] for col in FEATURE_COLUMNS]],
                            columns=FEATURE_COLUMNS)

    # Scale
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)[0]

    if prediction == 0:
        result = "✅ Credit Card Approved"
    else:
        result = "❌ Credit Card Rejected"

    return render_template(
        "result.html",
        prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)