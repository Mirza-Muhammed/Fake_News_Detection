# 📰 Fake News Detection System (Python + ML)

A complete, beginner-friendly project to classify news as **FAKE** or **REAL** using **Python**, **scikit-learn**, and **Flask**.  
This repo includes training code, a simple web app, and clear, step-by-step instructions.

---

## 🌿 Project Structure


fake_news_detection/
├── data/
│   └── news.csv         # Put your dataset here (text,label)
├── models/
│   ├── model.joblib     # Saved model (auto-generated after training)
│   └── vectorizer.joblib # Saved TF-IDF vectorizer
├── templates/
│   └── index.html       # Web UI for predictions
├── static/
│   └── styles.css       # (Optional) styles for the web app
├── app.py               # Flask app for inference
├── train.py             # Train/evaluate model
├── requirements.txt     # Python dependencies
└── README.md            # This file

### 2) Get the dataset
Use any **fake news dataset** (e.g., from Kaggle). Create a CSV at `data/news.csv` with two columns:

- `text`  → the article or headline text  
- `label` → one of: `FAKE`, `REAL`, `0`, or `1` (0=fake, 1=real)  

> If you have two files like `True.csv` and `Fake.csv`, just run `train.py` — it will auto-detect and combine them for you.

---

### 3) Train the model
```bash
python train.py

