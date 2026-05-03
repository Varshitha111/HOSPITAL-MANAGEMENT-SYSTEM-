import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# ================================================
# LOAD AND CLEAN (same as before)
# ================================================
data = pd.read_csv('imdb_top_1000.csv')
data = data.drop(columns=['Poster_Link', 'Overview'])
data['Runtime'] = data['Runtime'].str.replace(' min', '', regex=False)
data['Runtime'] = pd.to_numeric(data['Runtime'])
data['Gross'] = data['Gross'].str.replace(',', '', regex=False)
data['Gross'] = pd.to_numeric(data['Gross'], errors='coerce')
data['Gross'] = data['Gross'].fillna(data['Gross'].median())
data['Meta_score'] = data['Meta_score'].fillna(data['Meta_score'].median())
data['Certificate'] = data['Certificate'].fillna(data['Certificate'].mode()[0])
data['Released_Year'] = pd.to_numeric(data['Released_Year'], errors='coerce')
data['Released_Year'] = data['Released_Year'].fillna(data['Released_Year'].median())
data['Target'] = (data['IMDB_Rating'] >= 8.0).astype(int)

# ================================================
# STEP 1 — SELECT ONLY NUMERIC FEATURES
# ================================================
# ML models only understand numbers — not text!
# So we pick only numeric columns as our features

X = data[['Runtime', 'Meta_score', 'No_of_Votes', 'Gross', 'Released_Year']]
y = data['Target']

print("=" * 50)
print("FEATURES (X) — what we use to predict:")
print(X.columns.tolist())
print("Shape of X:", X.shape)

print("\nTARGET (y) — what we are predicting:")
print(y.value_counts())
print("Shape of y:", y.shape)

# ================================================
# STEP 2 — SPLIT INTO TRAIN AND TEST
# ================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,              # features
    y,              # target
    test_size=0.2,  # 20% for testing
    random_state=42 # fixed seed so results are same every run
)

print("\n" + "=" * 50)
print("TRAIN / TEST SPLIT RESULTS:")
print("=" * 50)
print(f"Total rows         : {len(X)}")
print(f"Training rows      : {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
print(f"Testing rows       : {len(X_test)}  ({len(X_test)/len(X)*100:.0f}%)")

print(f"\nX_train shape      : {X_train.shape}")
print(f"X_test shape       : {X_test.shape}")
print(f"y_train shape      : {y_train.shape}")
print(f"y_test shape       : {y_test.shape}")

print(f"\nTarget distribution in training:")
print(y_train.value_counts())
print(f"\nTarget distribution in testing:")
print(y_test.value_counts())

print("\nPhase 6 COMPLETE! Ready for ML models!")