import os
import joblib
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from palmreader.utils.image_utils import preprocess_image, extract_features

# Load label data (you must prepare this)
with open('data/labels.json') as f:
    labels_data = json.load(f)

X, y = [], []

for item in labels_data:
    image_path = os.path.join('data/images', item['image'])
    edges = preprocess_image(image_path)
    features = extract_features(edges)
    X.append(features)
    y.append(item['traits'])

mlb = MultiLabelBinarizer()
y_encoded = mlb.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

joblib.dump(clf, 'palmreader/models/saved_model.pkl')
joblib.dump(mlb, 'palmreader/models/label_encoder.pkl')

print("✅ Model and encoder saved successfully.")
