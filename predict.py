from flask import Flask, render_template, request, send_file, session
import pandas as pd
import joblib
import os

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.secret_key = "water_prediction_secret"

# Load model files
model = joblib.load("model.pkl")
accuracy = joblib.load("accuracy.pkl")

# Day Mapping
day_mapping = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

# Season Mapping
season_mapping = {
    "Spring": 0,
    "Summer": 1,
    "Autumn": 2,
    "Winter": 3,
}

latest_prediction = None
latest_input = {}


@app.route("/")
def home():

    history = []

    if os.path.exists("prediction_history.csv"):
        history = pd.read_csv("prediction_history.csv").tail(10).to_dict("records")

    return render_template(
        "index.html",
        prediction=None,
        accuracy=round(accuracy * 100, 2),
        history=history
    )


@app.route("/predict", methods=["POST"])
def predict():

    global latest_prediction, latest_input

    try:

        date = request.form["date"]
        day = request.form["day"]
        season = request.form["season"]

        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        rainfall = float(request.form["rainfall"])
        residents = int(request.form["residents"])

        date_num = pd.to_datetime(date).toordinal()

        day_value = day_mapping[day]
        season_value = season_mapping[season]

        prediction = model.predict([[
            date_num,
            day_value,
            season_value,
            temperature,
            humidity,
            rainfall,
            residents
        ]])

        latest_prediction = round(float(prediction[0]), 2)

        latest_input = {
            "Date": date,
            "Day": day,
            "Season": season,
            "Temperature": temperature,
            "Humidity": humidity,
            "Rainfall": rainfall,
            "Residents": residents
        }

        history = latest_input.copy()
        history["Prediction"] = latest_prediction

        history_df = pd.DataFrame([history])

        if os.path.exists("prediction_history.csv"):
            history_df.to_csv(
                "prediction_history.csv",
                mode="a",
                header=False,
                index=False
            )
        else:
            history_df.to_csv(
                "prediction_history.csv",
                index=False
            )

        history_table = pd.read_csv("prediction_history.csv").tail(10)

        return render_template(
            "index.html",
            prediction=latest_prediction,
            accuracy=round(accuracy * 100, 2),
            history=history_table.to_dict("records")
        )

    except Exception as e:
        return str(e)


@app.route("/download_pdf")
def download_pdf():

    global latest_prediction, latest_input

    if latest_prediction is None:
        return "Please predict first."

    filename = "Water_Consumption_Report.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("Water Consumption Prediction Report", styles["Title"]))

    for key, value in latest_input.items():
        story.append(Paragraph(f"<b>{key}</b>: {value}", styles["BodyText"]))

    story.append(
        Paragraph(
            f"<b>Predicted Water Consumption:</b> {latest_prediction} Liters",
            styles["Heading2"]
        )
    )

    doc.build(story)

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)