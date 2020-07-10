import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

th = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(th)
print(df.head())
print(df.dtypes)

# Calculate Correlation
print(df.corr)

# Numerical Variables
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

# Categorical Variables
# Calculate correlation for body-style and price
sns.boxplot(x="body-style", y="price", data=df)
plt.show()

# Calculate correlation for engine-location and price
sns.boxplot(x="engine-location", y="price", data=df)
plt.show()

# Descriptive Statistical analysis
print(df.describe())
print(df.describe(include=['object']))

# Count each characteristic in drive-wheels
print(df['drive-wheels'].value_counts())

# Convert previous command into dataframe
df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts.index.name = 'drive-wheels'

# Create group by body style with their average price
gb = df[["body-style", 'price']]
test2 = gb.groupby(["body-style"], as_index=False).mean()

# create pivot table
df_gptest = df[['drive-wheels', 'body-style', 'price']]
grouped_test1 = df_gptest.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')

# Convert NaN to 0
grouped_pivot = grouped_pivot.fillna(0)

# Create heatmap plot
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

# Pearson Correlation Coefficient and P-value for wheel-base, Horsepower, Length
# Width, Curb-weight, Engine-size, Bore, City-mpg and Highway-mpg
print("")
print("Pearson Correlation Coefficients")
print("wheel-base")
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print(pearson_coef, p_value)
print("")
print("Horsepower")
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print(pearson_coef, p_value)
print("")
print("Length")
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print(pearson_coef, p_value)
print("")
print("Width")
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print(pearson_coef, p_value)
print("")
print("Curb-weight")
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print(pearson_coef, p_value)
print("")
print("Engine-size")
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print(pearson_coef, p_value)
print("")
print("Bore")
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print(pearson_coef, p_value)
print("")
print("City-mpg")
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print(pearson_coef, p_value)
print("")
print("Highway-mpg")
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print(pearson_coef, p_value)

# Analysis of Variance (ANOVA) for categorical data, such as Drive-wheels.
test2 = df[['drive-wheels', 'price']].groupby(['drive-wheels'])
print(test2.head())
print(test2.get_group('4wd')['price'])

f_score, p_value = stats.f_oneway(test2.get_group('fwd')['price'], test2.get_group('rwd')['price'])
print(f_score, p_value)
f_score, p_value = stats.f_oneway(test2.get_group('fwd')['price'], test2.get_group('4wd')['price'])
print(f_score, p_value)
f_score, p_value = stats.f_oneway(test2.get_group('4wd')['price'], test2.get_group('rwd')['price'])
print(f_score, p_value)









