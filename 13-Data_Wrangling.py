import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


# Data formatting
print(df.dtypes)

# Convert data format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
print(df.dtypes)

# Data Standardization
# Convert mpg to L/100km
df['city-L/100km'] = 235 / df['city-mpg']
df['highway-L/100km'] = 235 / df['highway-mpg']

# Data Normalization
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()

# Binning: Convert continuous variables into discrete variables
df["horsepower"] = df["horsepower"].astype(int, copy=True)

plt.hist(df["horsepower"])
# x-axis and y-axis titles
plt.xlabel("Horsepower")
plt.ylabel("Count")
plt.title("Horsepower Bins")
plt.show()

ca = np.linspace(min(df['horsepower']), max(df['horsepower']), 4)
gn = ['Low', 'Medium', 'High']
df['h-binned'] = pd.cut(df['horsepower'], ca, labels=gn, include_lowest=True)
print(df[['horsepower', 'h-binned']].head(20))
print(df["h-binned"].value_counts())

plt.bar(gn, df["h-binned"].value_counts())
plt.xlabel("Horsepower")
plt.ylabel("Count")
plt.title("Horsepower bins")
plt.show()

# Plot histogram with 3 bins
plt.hist(df["horsepower"], bins=3)
plt.xlabel("Horsepower")
plt.ylabel("Count")
plt.title("Horsepower bins")
plt.show()

# Dummy variable: Convert categorical variable into numerical variable
print(df.columns)
dummy_v1 = pd.get_dummies(df["fuel-type"])
print(dummy_v1.head())

# Rename Columns
dummy_v1.rename(columns={'fuel-type-gas':'gas', 'fuel-type-diesel':'diesel'}, inplace=True)
print(dummy_v1.head())

# merge df and "dummy_v1"
df = pd.concat([df, dummy_v1], axis=1)

# Drop fuel-type from df
df.drop("fuel-type", axis=1, inplace=True)
print(df.dtypes)

# Save clean data into CSV
df.to_csv('clean_df.csv')




