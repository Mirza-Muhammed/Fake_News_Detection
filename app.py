import os
import joblib
from flask import Flask, render_template, request
from text_cleaner import TextCleaner

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")
VEC_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# Load model + vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VEC_PATH)
cleaner = TextCleaner()

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    proba = None

    if request.method == "POST":
        # ✅ FIXED: match the <textarea name="text"> in index.html
        user_input = request.form["text"]

        # Clean + vectorize
        cleaned = cleaner.transform([user_input])
        features = vectorizer.transform(cleaned)

        # Predict
        pred_label = model.predict(features)[0]   # "Fake" or "Real"
        pred_prob = model.predict_proba(features).max()  # highest probability

        prediction = pred_label
        proba = float(pred_prob)

    return render_template("index.html", prediction=prediction, proba=proba)

if __name__ == "__main__":
    app.run(debug=True)
