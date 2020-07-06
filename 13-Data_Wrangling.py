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




