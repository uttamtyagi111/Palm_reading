# 🖐️ Palmistry AI – Palm Reading Using Machine Learning

A Django web application that predicts palmistry-based traits by analyzing a user's palm image using image processing and a trained machine learning model.

---

## ✨ Features

- Upload any palm image (JPG/PNG)
- OpenCV-based image preprocessing and line detection
- Extracts palm features using Hough Transform
- Predicts 5 key palmistry traits:
  - General Palm Shape & Personality
  - Heart Line – Emotions & Relationships
  - Head Line – Thinking & Intelligence
  - Life Line – Vitality & Life Energy
  - Fate Line – Destiny & Life Path
- Displays predictions in the browser
- Optionally generate a PDF palm reading report

---

## 🏗️ Tech Stack

- 🐍 Python 3.8+
- 🧠 Scikit-learn (RandomForest + MultiOutputClassifier)
- 🖼️ OpenCV for image processing
- 🌐 Django (Web framework)
- 📦 joblib (model serialization)
- 📝 HTML/CSS for UI (Django templates)

---

## 🚀 Getting Started
bash

### 1. Clone the Repository
git colne https://github.com/uttamtyagi111/Palm_reading.git

### 2. Install the Requirements
pip install -r requirements.txt