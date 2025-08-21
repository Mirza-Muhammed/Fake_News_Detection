import pandas as pd

# Load both datasets
fake = pd.read_csv("data/Fake.csv")
true = pd.read_csv("data/True.csv")

# Assign labels
fake['label'] = 1   # Fake news
true['label'] = 0   # Real news

# Merge title + text into one column
fake['text'] = fake['title'] + " " + fake['text']
true['text'] = true['title'] + " " + true['text']

# Keep only required columns
fake = fake[['text', 'label']]
true = true[['text', 'label']]

# Combine
df = pd.concat([fake, true])

# Shuffle
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save
df.to_csv("data/news.csv", index=False)

print("✅ news.csv created with", len(df), "rows and columns:", df.columns.tolist())
