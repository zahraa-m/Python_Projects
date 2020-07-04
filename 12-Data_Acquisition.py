import pandas as pd
URL="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(URL, header=None)
print("the first 5 rows")
print(df.head(5))

# Add headers to the data
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns=headers
print(df.head(5))

# Drop missing values in price
df.dropna(subset=["price"], axis=0)

# Get columns name
print(df.info())

# Save the new data frame into csv file
df.to_csv("new_data.csv", index=False)

# Show statistical summary
print(df.describe())

# Show all
print(df.describe(include="all"))

# describe only length and compression-ratio
print(df[['length', 'compression-ratio']].describe())



