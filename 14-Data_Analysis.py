import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

th = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(th)
print(df.head())
print(df.dtypes)

# Calculate Correlation
print(df.corr)

# calculate correlation for bore, stroke, compression-ratio and horsepower
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()

# Obtain the linear relationship between engine-size and price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.show()
print(df[["engine-size", "price"]].corr())

# Obtain the linear relationship between highway-mpg and price
sns.regplot(x="highway-mpg", y="price", data=df)
plt.show()
print(df[["highway-mpg", "price"]].corr())

# Obtain the linear relationship between stroke and price
sns.regplot(x="stroke", y="price", data=df)
plt.show()
print(df[['stroke', 'price']].corr())





