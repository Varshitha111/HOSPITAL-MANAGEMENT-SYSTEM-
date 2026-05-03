import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt




data = pd.read_csv('imdb_top_1000.csv')
data = data.drop(columns=['Poster_Link', 'Overview'])
data['Runtime']=data['Runtime'].str.replace(' min', '', regex=False)
data['Runtime']=pd.to_numeric(data['Runtime'])
data['Gross']=data['Gross'].str.replace(',', '', regex=False)
data['Gross']=pd.to_numeric(data['Gross'], errors='coerce')
gross_median=data['Gross'].median()         
data['Gross']=data['Gross'].fillna(gross_median)  
print("Gross missing after fix:", data['Gross'].isnull().sum())
data['Meta_score']=data['Meta_score'].fillna(data['Meta_score'].median())
data['Certificate']= data['Certificate'].fillna(data['Certificate'].mode()[0])
data['Released_Year']=pd.to_numeric(data['Released_Year'], errors='coerce')
data['Released_Year']=data['Released_Year'].fillna(data['Released_Year'].median())
data['Target'] = (data['IMDB_Rating'] >= 8.0).astype(int)
print(f"Total missing : {data.isnull().sum().sum()}")
print(f"Runtime dtype : {data['Runtime'].dtype}")
print(f"Gross dtype   : {data['Gross'].dtype}")
print(f"Shape         : {data.shape}")
print("\nTarget counts:")
print(data['Target'].value_counts())
print("\nAll missing values:")
print(data.isnull().sum())
print("\nPreview:")
print(data[['Series_Title','Runtime','Gross','Meta_score','Target']].head(3))
# using train test split
X = data[['Runtime', 'Meta_score', 'No_of_Votes', 'Gross', 'Released_Year']]
y = data['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model
model=LogisticRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
plt.boxplot(X_train['Gross'])
plt.title("Gross Outliers")
plt.show()