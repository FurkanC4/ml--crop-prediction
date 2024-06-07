import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import statistics
import joblib
from sklearn.model_selection import train_test_split

df = pd.read_csv("soil.csv")


x = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df["label"]


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=42)


from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
x_train_scaled =scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
log =LogisticRegression(max_iter = 1000)
from sklearn.ensemble import RandomForestClassifier

RandomForest = RandomForestClassifier(n_estimators=20, random_state=None)

# Fitting the training set to create a model
RandomForest.fit(x_train,y_train)
# Using test(x) to find y
ypred = RandomForest.predict(x_test)

#accuracy = metrics.accuracy_score(ypred, y_test)


file = "finall.sav"


joblib.dump(RandomForest,file)