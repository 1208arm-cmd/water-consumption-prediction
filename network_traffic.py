import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 1. Load Dataset
data = pd.read_csv("dataset/network_traffic.csv")

print("Dataset:")
print(data)

# 2. Convert Traffic Type into numbers
encoder = LabelEncoder()
data["Traffic_Type"] = encoder.fit_transform(data["Traffic_Type"])

# 3. Separate Features and Target
X = data.drop("Traffic_Type", axis=1)
y = data["Traffic_Type"]

# 4. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Create ML Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 6. Train Model
model.fit(X_train, y_train)

# 7. Make Predictions
y_pred = model.predict(X_test)

# 8. Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy * 100, "%")

# 9. Classification Report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        labels=sorted(y.unique()),
        target_names=encoder.classes_,
        zero_division=0
    )
)

# 10. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(7, 5))
plt.imshow(cm)
plt.title("Network Traffic Classification")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()

plt.xticks(range(len(encoder.classes_)), encoder.classes_, rotation=45)
plt.yticks(range(len(encoder.classes_)), encoder.classes_)

plt.tight_layout()
plt.show()


# 11. New Traffic Prediction
new_traffic = [[600, 10, 55, 6]]

prediction = model.predict(new_traffic)

traffic_name = encoder.inverse_transform(prediction)

print("\nNew Traffic Prediction:", traffic_name[0])