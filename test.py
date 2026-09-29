import os
import pandas as pd

path = r"F:\Water_Consumption_Prediction\dataset.csv"

print("Exists:", os.path.exists(path))
print("Is file:", os.path.isfile(path))

df = pd.read_csv(path)
print(df.head())