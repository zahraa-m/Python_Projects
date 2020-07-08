# Data Science with Python
I have used automobile [Data](https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv) to practice Python with Data Science. The Data set has 26 attributes (columns) as shown in the table below and 205 instances (rows). The target attribute is the price of cars. 

| Column            | Data type |
|-------------------|-----------|
| symboling         | int64     |
| normalized-losses | object    |
| make              | object    |
| fuel-type         | object    |
| aspiration        | object    |
| num-of-doors      | object    |
| body-style        | object    |
| drive-wheels      | object    |
| engine-location   | object    |
| wheel-base        | float64   |
| length            | float64   |
| width             | float64   |
| height            | float64   |
| curb-weight       | int64     |
| engine-type       | object    |
| num-of-cylinders  | object    |
| engine-size       | int64     |
| fuel-system       | object    |
| bore              | object    |
| stroke            | object    |
| compression-ratio | float64   |
| horsepower        | object    |
| peak-rpm          | object    |
| city-mpg          | int64     |
| highway-mpg       | int64     |
| price             | object    |


## 1. Data Wrangling
### Handling Missing Data
- **Replaced "?" with NaN**
- **Mean**: Replaced NaN values in normalized-losses, stroke, bore, horsepower and peak-rpm columns to **mean** value of each column.
- **The most frequent value**: Replaced NaN values in num-of-doors to the most frequent value, which is **four**.
- **Drop**: Dropped 2 missing values (deleted 2 rows) in **price** column.

### Data Formatting
- **Float**: Converted price, bore, stroke and peak-rpm into float.
- **Integer**: Converted normalized-losses into integer.
- **Mpg to L/100km**: Converted city-mpg and highway-mpg from mpg to L/100km.
- **Binning**: Converted **horsepower** from continuous variable to discrete variable.
- **Dummy variable**: Converted **fuel-type** from categorical variable to numerical variable. Where gas is 1 and diesel is 0.

### Data Normalization
I have normalized **length**, **width** and **height** columns. 

## 2. Data Analysis

## 3. Model Development

## 4. Model Evaluation


