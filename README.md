# 📰 Fake News Detection System (Python + ML)

A complete, beginner-friendly project to classify news as **FAKE** or **REAL** using **Python**, **scikit-learn**, and **Flask**.  
This repo includes training code, a simple web app, and clear, step-by-step instructions.

---

## 🧩 Project Structure

```text
fake_news_detection/
├─ data/
│  └─ news.csv                 # Put your dataset here (text,label)
├─ models/
│  ├─ model.joblib             # Saved model (auto-generated after training)
│  └─ vectorizer.joblib        # Saved TF-IDF vectorizer
├─ templates/
│  └─ index.html               # Web UI for predictions
├─ static/
│  └─ styles.css               # (Optional) styles for the web app
├─ app.py                      # Flask app for inference
├─ train.py                    # Train/evaluate model
├─ requirements.txt            # Python dependencies
└─ README.md                   # This file
## ✅ Step-by-Step Guide

### 1) Create environment & install dependencies
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
### 2) Get the dataset
Use any **fake news dataset** (e.g., from Kaggle). Create a CSV at `data/news.csv` with two columns:

- `text`  → the article or headline text  
- `label` → one of: `FAKE`, `REAL`, `0`, or `1` (0=fake, 1=real)  

> If you have two files like `True.csv` and `Fake.csv`, just run `train.py` — it will auto-detect and combine them for you.

---

### 3) Train the model
```bash
python train.py

⚡ This will render **exactly like your screenshot** with proper formatting.  

👉 Do you want me to now prepare **Step 4 (Run the web app)** and **Step 5 (Optional deploy)** in the same style so the workflow looks complete?


