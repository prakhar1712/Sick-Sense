import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import joblib
from sklearn import preprocessing
from sklearn.metrics import classification_report, accuracy_score, f1_score

df = pd.read_csv('survey lung cancer.csv')

le = preprocessing.LabelEncoder()
df['GENDER'] = le.fit_transform(df['GENDER'])
df['LUNG_CANCER'] = le.fit_transform(df['LUNG_CANCER'])
df['SMOKING'] = le.fit_transform(df['SMOKING'])
df['YELLOW_FINGERS'] = le.fit_transform(df['YELLOW_FINGERS'])
df['ANXIETY'] = le.fit_transform(df['ANXIETY'])
df['PEER_PRESSURE'] = le.fit_transform(df['PEER_PRESSURE'])
df['CHRONIC DISEASE'] = le.fit_transform(df['CHRONIC DISEASE'])
df['FATIGUE '] = le.fit_transform(df['FATIGUE '])
df['ALLERGY '] = le.fit_transform(df['ALLERGY '])
df['WHEEZING'] = le.fit_transform(df['WHEEZING'])
df['ALCOHOL CONSUMING'] = le.fit_transform(df['ALCOHOL CONSUMING'])
df['COUGHING'] = le.fit_transform(df['COUGHING'])
df['SHORTNESS OF BREATH'] = le.fit_transform(df['SHORTNESS OF BREATH'])
df['SWALLOWING DIFFICULTY'] = le.fit_transform(df['SWALLOWING DIFFICULTY'])
df['CHEST PAIN'] = le.fit_transform(df['CHEST PAIN'])
df['LUNG_CANCER'] = le.fit_transform(df['LUNG_CANCER'])


df_new = df.drop(columns=['GENDER', 'AGE', 'SMOKING',
                 'SHORTNESS OF BREATH', 'ANXIETY', 'CHRONIC DISEASE', 'PEER_PRESSURE'])
# Splitting independent and dependent variables
X = df_new.drop('LUNG_CANCER', axis=1)
y = df_new['LUNG_CANCER']

# Splitting data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)

# Training
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Predicting result using testing data
y_rf_pred = rf_model.predict(X_test)
print(rf_model.score(X_test, y_test))

# filename = 'finalized4_model.sav'
# joblib.dump(rf_model, filename)
