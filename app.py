from flask import Flask, render_template, request, send_file, session
import pandas as pd
import joblib
import os

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ==========================
# Create Flask App
# ==========================

app = Flask(__name__)

# ==========================
# Load ML Model
# ==========================

model = joblib.load("model.pkl")
day_encoder = joblib.load("day_encoder.pkl")
season_encoder = joblib.load("season_encoder.pkl")
accuracy = joblib.load("accuracy.pkl")

# ==========================
# Global Variables
# ==========================

latest_prediction = None
latest_input = {}

algorithm = "Random Forest Regressor"
training_records = 400
testing_records = 100
total_records = 500

# ==========================
# Load Dataset
# ==========================

data = pd.read_csv("dataset.csv")

data["Date"] = pd.to_datetime(data["Date"])
data["Month"] = data["Date"].dt.strftime("%b")

# ==========================
# Charts
# ==========================

monthly = data.groupby("Month")["WaterConsumption"].mean()

monthly_labels = monthly.index.tolist()
monthly_values = monthly.values.tolist()

temp_labels = data["Temperature"].tolist()
temp_values = data["WaterConsumption"].tolist()

rain_labels = data["Rainfall"].tolist()
rain_values = data["WaterConsumption"].tolist()

pie_labels = [
    "Kitchen",
    "Bathroom",
    "Laundry",
    "Garden"
]

pie_values = [35, 40, 15, 10]

# ==========================
# Model Information
# ==========================

algorithm = "Random Forest Regressor"
training_records = 400
testing_records = 100
total_records = 500

# ==========================
# Home
# ==========================

@app.route("/")
def home():

    if os.path.exists("prediction_history.csv"):
        history_table = pd.read_csv("prediction_history.csv").tail(10)
    else:
        history_table = pd.DataFrame()

    return render_template(
        "index.html",

        prediction=None,

        accuracy=round(accuracy * 100, 2),

        algorithm=algorithm,
        training_records=training_records,
        testing_records=testing_records,
        total_records=total_records,

        monthly_labels=monthly_labels,
        monthly_values=monthly_values,

        temp_labels=temp_labels,
        temp_values=temp_values,

        rain_labels=rain_labels,
        rain_values=rain_values,

        pie_labels=pie_labels,
        pie_values=pie_values,

        history=history_table.to_dict(orient="records")
    )
# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    global latest_prediction, latest_input

    date = request.form["date"]
    day = request.form["day"]
    season = request.form["season"]

    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    rainfall = float(request.form["rainfall"])
    residents = int(request.form["residents"])

    # Convert date
    date_num = pd.to_datetime(date).toordinal()

    # Encode
    day_encoded = day_encoder.transform([day])[0]
    season_encoded = season_encoder.transform([season])[0]

    # Predict
    prediction = model.predict([[
        date_num,
        day_encoded,
        season_encoded,
        temperature,
        humidity,
        rainfall,
        residents
    ]])[0]

    latest_prediction = round(prediction, 2)

    latest_input = {
        "Date": date,
        "Day": day,
        "Season": season,
        "Temperature": temperature,
        "Humidity": humidity,
        "Rainfall": rainfall,
        "Residents": residents
    }

    # Save history
    history = {
        "Date": date,
        "Day": day,
        "Season": season,
        "Temperature": temperature,
        "Humidity": humidity,
        "Rainfall": rainfall,
        "Residents": residents,
        "Prediction": latest_prediction
    }

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

        monthly_labels=monthly_labels,
        monthly_values=monthly_values,

        temp_labels=temp_labels,
        temp_values=temp_values,

        rain_labels=rain_labels,
        rain_values=rain_values,

        pie_labels=pie_labels,
        pie_values=pie_values,

        history=history_table.to_dict(orient="records")
    )

# ==========================
# Download PDF
# ==========================

@app.route("/download_pdf")
def download_pdf():

    global latest_prediction, latest_input

    if latest_prediction is None:
        return "Please make a prediction first."

    pdf_file = os.path.join(os.getcwd(), "Water_Consumption_Report.pdf")

    doc = SimpleDocTemplate(pdf_file)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("Water Consumption Prediction Report", styles["Title"]))
    story.append(Paragraph(f"Date: {latest_input['Date']}", styles["BodyText"]))
    story.append(Paragraph(f"Day: {latest_input['Day']}", styles["BodyText"]))
    story.append(Paragraph(f"Season: {latest_input['Season']}", styles["BodyText"]))
    story.append(Paragraph(f"Temperature: {latest_input['Temperature']} °C", styles["BodyText"]))
    story.append(Paragraph(f"Humidity: {latest_input['Humidity']} %", styles["BodyText"]))
    story.append(Paragraph(f"Rainfall: {latest_input['Rainfall']} mm", styles["BodyText"]))
    story.append(Paragraph(f"Residents: {latest_input['Residents']}", styles["BodyText"]))
    story.append(Paragraph(
        f"<b>Predicted Water Consumption: {latest_prediction} Liters</b>",
        styles["Heading2"]
    ))

    doc.build(story)

    return send_file(
        pdf_file,
        as_attachment=True,
        download_name="Water_Consumption_Report.pdf"
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)