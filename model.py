import joblib
import json
import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Create models directory if it doesn't exist
os.makedirs('model', exist_ok=True)

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a random forest classifier
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model and target names
print("Saving model...")
joblib.dump(model, 'model/model.joblib')
print("Model saved")
with open('model/target_names.json', 'w') as f:
    json.dump(iris.target_names.tolist(), f)
print("Target names saved")