import pandas as pd
import random
from datetime import datetime, timedelta

# ==========================
# Settings
# ==========================

random.seed(42)

NUM_ROWS = 500
START_DATE = datetime(2025, 1, 1)

# ==========================
# Season Mapping
# ==========================

seasons = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Summer", 4: "Summer", 5: "Summer",
    6: "Monsoon", 7: "Monsoon", 8: "Monsoon",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

data = []

# ==========================
# Generate Data
# ==========================

for i in range(NUM_ROWS):

    current_date = START_DATE + timedelta(days=i)

    date = current_date.strftime("%Y-%m-%d")
    day = current_date.strftime("%A")
    season = seasons[current_date.month]

    # Weather based on season
    if season == "Summer":
        temperature = random.randint(32, 45)
        humidity = random.randint(35, 60)
        rainfall = random.randint(0, 10)

    elif season == "Monsoon":
        temperature = random.randint(24, 34)
        humidity = random.randint(70, 95)
        rainfall = random.randint(20, 120)

    elif season == "Winter":
        temperature = random.randint(15, 28)
        humidity = random.randint(40, 70)
        rainfall = random.randint(0, 20)

    else:  # Autumn
        temperature = random.randint(22, 35)
        humidity = random.randint(45, 75)
        rainfall = random.randint(0, 30)

    residents = random.randint(1, 8)

    # Realistic daily water consumption
    base = residents * 130
    temp_effect = temperature * 5
    humidity_effect = humidity * 0.4
    rainfall_effect = rainfall * 1.5
    noise = random.randint(-25, 25)

    water_consumption = (
        base
        + temp_effect
        - humidity_effect
        - rainfall_effect
        + noise
    )

    water_consumption = round(max(100, water_consumption), 1)

    data.append([
        date,
        day,
        season,
        temperature,
        humidity,
        rainfall,
        residents,
        water_consumption
    ])

# ==========================
# Create DataFrame
# ==========================

df = pd.DataFrame(data, columns=[
    "Date",
    "Day",
    "Season",
    "Temperature",
    "Humidity",
    "Rainfall",
    "Residents",
    "WaterConsumption"
])

# ==========================
# Save Dataset
# ==========================

df.to_csv("dataset.csv", index=False)

# ==========================
# Display Information
# ==========================

print("=" * 50)
print("Water Consumption Dataset Generated")
print("=" * 50)

print(f"Total Records : {len(df)}")
print(f"Columns       : {len(df.columns)}")
print("File Saved    : dataset.csv")

print("=" * 50)

print("\nFirst 10 Records\n")
print(df.head(10))

print("\nDataset Statistics\n")
print(df.describe())