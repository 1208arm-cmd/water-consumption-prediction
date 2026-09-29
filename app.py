from flask import Flask, render_template, request
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


app = Flask(__name__)


# Load dataset
data = pd.read_csv("dataset/network_traffic.csv")


# Encode target
encoder = LabelEncoder()
data["Traffic_Type"] = encoder.fit_transform(data["Traffic_Type"])


# Features and target
X = data[
    [
        "Packet_Size",
        "Duration",
        "Packets_Per_Second",
        "Protocol"
    ]
]

y = data["Traffic_Type"]


# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    packet_size = float(request.form["packet_size"])
    duration = float(request.form["duration"])
    packets = float(request.form["packets"])
    protocol = int(request.form["protocol"])

    input_data = [[
        packet_size,
        duration,
        packets,
        protocol
    ]]

    prediction = model.predict(input_data)

    result = encoder.inverse_transform(prediction)[0]

    return render_template(
        "index.html",
        prediction=result
    )


if __name__ == "__main__":
    app.run(debug=True)