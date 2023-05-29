import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df['bmi'].fillna(df['bmi'].mode()[0], inplace=True)
df = df.drop(columns=['ever_married', 'work_type',
             'Residence_type', 'smoking_status', 'id'], axis=1)
df.replace({'gender': {'Male': 0, 'Female': 1, 'Other': 2}}, inplace=True)
X = df.drop(columns=['hypertension'], axis=1)
Y_hypertension = df['hypertension']

scaler = StandardScaler()
scaler.fit(X)
standard = scaler.transform(X)
X = standard
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y_hypertension, test_size=0.2, stratify=Y_hypertension, random_state=2)

model = svm.SVC(kernel='linear')
model.fit(X_train, Y_train)
X_train_prediction = model.predict(X_train)
train_data_accuracy = accuracy_score(X_train_prediction, Y_train)
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print((test_data_accuracy) * 100)

filename = 'finalized3_model.sav'
joblib.dump(model, filename)
