# predict the Price

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

URL = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(URL)
print(df.head())

# predict Price By using Linear Regression model
# Simple Linear Regression (SLR) | independent variable = Highway-mpg and dependent = Price
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm
x = df[['highway-mpg']]
y = df[['price']]
lm.fit(x, y)
y_new = lm.predict(x)
print(y_new[0:6])
print("")
print("The final linear model is")
print("y_new=", lm.intercept_[0], lm.coef_.item(0), "* x_new")

