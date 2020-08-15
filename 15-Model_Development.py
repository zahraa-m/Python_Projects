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
x = df[['engine-size']]
y = df[['price']]
lm.fit(x, y)
y_new = lm.predict(x)
print(y_new[0:6])
print("")
print("The final linear model is")
print("y_new=", lm.intercept_[0], lm.coef_.item(0), "* x_new")

# Multiple Linear Regression (MLR) | independent variables = Highway-mpg and normalized-losses, dependent = Price
lm.fit(df[['normalized-losses', 'highway-mpg']], df[['price']])
print("The final linear model is")
print("intercept=", lm.intercept_, "Coefficients=", lm.coef_)

# Evaluate Linear models by visualization
import seaborn as sns
import matplotlib.pyplot as plt

w = 8
h = 6
plt.figure(figsize=(w, h))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0, )
plt.show()

sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0, )
plt.show()

# Calculate correlation between price and highway-mpg as well peak-rpm
print(df[['highway-mpg', 'peak-rpm', 'price']].corr())

# Evaluate the model by finding the residuals plot for SLR
sns.residplot(df[['highway-mpg']], df[['price']])
plt.show()

# Evaluate the model by finding the distribution plot for MLR
y_new = lm.predict(df[['normalized-losses', 'highway-mpg']])
ax1 = sns.distplot(df['price'], hist=False, color='r', label='Actual Values')
sns.distplot(y_new, hist=False, color='g', label='Fitted Values', ax=ax1)
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')
plt.show()


# Model non-linear (Polynomial) regression
def plotpolly(model, independent_variable, dependent_variable, name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)
    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, '-')
    plt.xlabel(name)
    plt.ylabel('Price of Cars')
    plt.show()
    plt.close()


# Create the model
x = df['highway-mpg']
y = df['price']
n = np.polyfit(x, y, 11)
m = np.poly1d(n)

# Plot polynomial model by using plotpolly function
plotpolly(m, x, y, 'highway-mpg')
