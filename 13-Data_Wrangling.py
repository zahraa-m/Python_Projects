import pandas as pd
import numpy as np
import matplotlib.pylab as plt

fn = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
hn = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(fn, names=hn)
print(df.head())

# Handling Missing Values
# Replace ? to NaN
df.replace("?", np.nan, inplace=True)
print(df.head(5))

# Count missing values
md = df.isnull()
print(md.head(5))
for column in md.columns.values.tolist():
    print(column)
    print(md[column].value_counts())
    print(" ")


# Calculate the mean for normalized-losses, stroke, bore, horsepower and peak-rpm
avg_norm = df["normalized-losses"].astype("float").mean(axis=0)
print("normalized-losses mean:", avg_norm)
df["normalized-losses"].replace(np.nan, avg_norm, inplace=True)

avg_bore = df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True)

avg_stroke = df['stroke'].astype('float').mean(axis=0)
print("Average of stroke:", avg_stroke)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# Replace missing values with most freq value
print(df["num-of-doors"].value_counts().idxmax())
df["num-of-doors"].replace(np.nan, 'four', inplace=True)

# Drop missing value in price column
df.dropna(subset=["price"], axis=0, inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)


