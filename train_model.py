import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# ==========================
# Load Dataset
# ==========================

data = pd.read_csv("dataset.csv")

# ==========================
# Data Preprocessing
# ==========================

# Convert Date to numeric
data["Date"] = pd.to_datetime(data["Date"])
data["Date"] = data["Date"].map(pd.Timestamp.toordinal)

# Encode Day
day_encoder = LabelEncoder()
data["Day"] = day_encoder.fit_transform(data["Day"])

# Encode Season
season_encoder = LabelEncoder()
data["Season"] = season_encoder.fit_transform(data["Season"])

# ==========================
# Features & Target
# ==========================

X = data[[
    "Date",
    "Day",
    "Season",
    "Temperature",
    "Humidity",
    "Rainfall",
    "Residents"
]]

y = data["WaterConsumption"]

# ==========================
# Split Dataset
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================
# Train Model
# ==========================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# Evaluate Model
# ==========================

predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("=" * 45)
print("Water Consumption Prediction Model")
print("=" * 45)

print(f"R² Score      : {r2:.4f}")
print(f"MAE           : {mae:.2f}")
print(f"RMSE          : {rmse:.2f}")

print("=" * 45)

# ==========================
# Save Files
# ==========================

joblib.dump(model, "model.pkl")
joblib.dump(day_encoder, "day_encoder.pkl")
joblib.dump(season_encoder, "season_encoder.pkl")
joblib.dump(r2, "accuracy.pkl")

print("Model saved successfully.")
print("day_encoder.pkl saved.")
print("season_encoder.pkl saved.")
print("accuracy.pkl saved.")

# ==========================
# Feature Importance
# ==========================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")
print("----------------------------")
print(importance)