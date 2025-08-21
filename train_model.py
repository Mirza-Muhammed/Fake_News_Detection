import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, f1_score
from text_cleaner import TextCleaner

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

FAKE_PATH = os.path.join(DATA_DIR, "Fake.csv")
TRUE_PATH = os.path.join(DATA_DIR, "True.csv")

print("[INFO] Loading datasets...")
fake_df = pd.read_csv(FAKE_PATH)
true_df = pd.read_csv(TRUE_PATH)

# Label data
fake_df["label"] = "Fake"
true_df["label"] = "Real"

# Combine and shuffle
df = pd.concat([fake_df, true_df], ignore_index=True)
df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)

# Combine title + text
df["content"] = (df["title"].fillna("") + " " + df["text"].fillna("")).str.strip()

# Clean text
cleaner = TextCleaner()
print("[INFO] Cleaning text...")
df["content_clean"] = cleaner.transform(df["content"].tolist())

X = df["content_clean"].values
y = df["label"].values

# Split
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Vectorizer
vectorizer = TfidfVectorizer(max_features=50000, ngram_range=(1,2), min_df=2)

print("[INFO] Vectorizing...")
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)

# Model
model = MultinomialNB(alpha=0.1)
print("[INFO] Training model...")
model.fit(X_train_vec, y_train)

# Evaluate
print("[INFO] Evaluating...")
y_pred = model.predict(X_val_vec)
acc = accuracy_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred, pos_label="Real")
print(f"[METRICS] Accuracy: {acc:.4f} | F1 (Real): {f1:.4f}")
print(classification_report(y_val, y_pred))

# Save
model_path = os.path.join(MODEL_DIR, "best_model.pkl")
vec_path = os.path.join(MODEL_DIR, "vectorizer.pkl")
joblib.dump(model, model_path)
joblib.dump(vectorizer, vec_path)

print(f"[OK] Saved model to {model_path}")
print(f"[OK] Saved vectorizer to {vec_path}")
