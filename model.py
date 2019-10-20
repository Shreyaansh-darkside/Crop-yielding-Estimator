# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 08:48:27 2019

@author: Shreyaansh
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('corn.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

sc = StandardScaler()
X = sc.fit_transform(X)

#Splitting Training and Test Set

#Since we have a very small dataset, we will train our model with all availabe data.

poly_reg = PolynomialFeatures(degree =2 ,interaction_only=False, include_bias=True)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X, y)

reg = LinearRegression().fit(X_poly, y)

y_pred = reg.predict(poly_reg.fit_transform(X))

r2_score(y,y_pred)

# Saving model to disk
pickle.dump(reg, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict(poly_reg.fit_transform([[7.77, 1.02]])))