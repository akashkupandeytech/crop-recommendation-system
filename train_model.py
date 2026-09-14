import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
data = pd.read_csv("dataset/Crop_recommendation.csv")

print("Dataset loaded successfully!")
print("shape:", data.shape)
print("\n first 5 rows:")
print(data.head())

# 2. Separate features and target
X = data.drop("label", axis=1)
y = data["label"]

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 4. Create model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

# 5. Train model
print("\nTraining model...")
model.fit(X_train, y_train)

# 6. Test model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. Save model
joblib.dump(model, "crop_model.pkl")

print("\nModel saved successfully as crop_model.pkl")