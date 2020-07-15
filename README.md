# Data Science with Python
This repository is for Data Analysis with Python [course](https://cognitiveclass.ai/courses/data-analysis-python). I took this course for practicing Data Science. I used automobile [Data](https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv) that has 26 attributes (columns) as shown in the table below and 205 instances (rows). The goal is to create models for predicting the price of cars, as well as, evaluate the model. 

| Column | symboling | normalized-losses | make | fuel-type | aspiration | num-of-doors | body-style | drive-wheels | engine-location | wheel-base | length | width | height | curb-weight | engine-type | num-of-cylinders | engine-size | fuel-system | bore | stroke | compression-ratio | horsepower | peak-rpm | city-mpg | highway-mpg | price |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| Data type | int64 | object | object | object | object | object | object | object | object | float64 | float64 | float64 | float64 | int64 | object | object | int64 | object | object | object | float64 | object | object | int64 | int64 | object |
<br/>


## 1. Data Wrangling
### Handling Missing Data
- **Replace "?" with NaN**
- **Mean**: Replace NaN values in normalized-losses, stroke, bore, horsepower and peak-rpm columns to **mean** value of each column.
- **The most frequent value**: Replace NaN values in num-of-doors to the most frequent value, which is **four**.
- **Drop**: Drop 2 missing values (deleted 2 rows) in **price** column.

### Data Formatting
- **Float**: Convert price, bore, stroke and peak-rpm into float.
- **Integer**: Convert normalized-losses into integer.
- **Mpg to L/100km**: Convert city-mpg and highway-mpg from mpg to L/100km.
- **Binning**: Convert **horsepower** from continuous variable to discrete variable.
- **Dummy variable**: Convert **fuel-type** from categorical variable to numerical variable. Where gas is 1 and diesel is 0.

### Data Normalization
I normalize **length**, **width** and **height** columns, by dividing each value to maximum value.
<br/>
<br/>

## 2. Data Analysis
- **Linear relationship**: Obtaine the linear relationship between Price and each of these attributes: Engine-size, Highway-mpg and Stroke. There are positive linear relationship between Price and Engine-size, negative linear relationship between Price and Highway-mpg and weak linear relationship between Price and Stroke, as shown respectively in the figures below.

| <img width="300" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_1.png" alt="The linear relationship between Price and engine-size"/> | <img width="300" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_2.png" alt="The linear relationship between Price and engine-size"/> | <img width="300" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_3.png" alt="The linear relationship between Price and engine-size"/> |
|-|-|-|

<br/>
 
- **Pearson correlation**: I calculate Pearson Correlation Coefficient and P-value between Price and each of these attributes: Wheel-base, Horsepower, Length, Width, Curb-weight, Engine-size, Bore, City-mpg and Highway-mpg.
- **Correlation in Categorical Variables**: By using boxplot, I illustrate the correlation between Price and Body-style first and Engine-location second, as shown in the figures below. From the plots we can conclude that the Engine-location is a good predictor for the Price, because its distrubation covers almost all price range, where Body-style categories have a notable overlap.

| <img width="350" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_4.png" alt="Correlation between Price and Body-style"/> | <img width="350" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_5.png" alt="Correlation between Price and Engine-location"/> |
|-|-|

- **ANOVA**: I calculate F-test score and P-value between Drive-wheels and Price. It shows high correlation as F-test score is 67.95. Also, P_value is near to 0, which means statistical significance between the two varibles. Additionally, Drive-wheels has 3 categories: fwd, rwd and 4wd where I calculate F-test score and P-value between fwd and rwd Price first, 4wd Price second and between rwd and 4rwd Price. Fwd vs. rwd has the higher correlation where 4wd vs. rwd has weak correlation and fwd vs. 4wd has no correlation.
<br/>
<br/>

## 3. Model Development

## 4. Model Evaluation


