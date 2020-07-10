# Data Science with Python
This repository is for Data Analysis with Python [course](https://cognitiveclass.ai/courses/data-analysis-python). I have took this course for practicing Data Science. I used automobile [Data](https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv) that has 26 attributes (columns) as shown in the table below and 205 instances (rows). The goal is to create models for predicting the price of cars, as well as, evaluate the model. 

| Column | symboling | normalized-losses | make | fuel-type | aspiration | num-of-doors | body-style | drive-wheels | engine-location | wheel-base | length | width | height | curb-weight | engine-type | num-of-cylinders | engine-size | fuel-system | bore | stroke | compression-ratio | horsepower | peak-rpm | city-mpg | highway-mpg | price |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| Data type | int64 | object | object | object | object | object | object | object | object | float64 | float64 | float64 | float64 | int64 | object | object | int64 | object | object | object | float64 | object | object | int64 | int64 | object |
</br>


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
I have normalized **length**, **width** and **height** columns, by dividing each value to maximum value.
</br>
</br>

## 2. Data Analysis
- **Descriptive Statistical analysis**:
- **Linear relationship**:
- **Pearson Correlation**:
- **ANOVA**:

## 3. Model Development

## 4. Model Evaluation


