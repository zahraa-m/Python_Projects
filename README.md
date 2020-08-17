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
- **Linear relationship**: Obtain the linear relationship between Price and each of these attributes: Engine-size, Highway-mpg and Stroke. There are positive linear relationship between Price and Engine-size, negative linear relationship between Price and Highway-mpg and weak linear relationship between Price and Stroke, as shown respectively in the figures below.

| <img width="300" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_1.png" alt="The linear relationship between Price and engine-size"/> | <img width="300" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_2.png" alt="The linear relationship between Price and engine-size"/> | <img width="300" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_3.png" alt="The linear relationship between Price and engine-size"/> |
|-|-|-|

<br/>
<br/>
<br/>

- **Pearson correlation**: I calculate Pearson Correlation Coefficient and P-value between Price and each of these attributes: Wheel-base, Horsepower, Length, Width, Curb-weight, Engine-size, Bore, City-mpg and Highway-mpg as shown in the table below.

| Features | Pearson Correlation Coeff. | P-value |
|:-:|:-:|:-:|
| Wheel-base | 0.58464 | 8.07648e-20 |
| Horsepower | 0.80957 | 6.36905e-48 |
| Length | 0.69062 | 8.01647e-30 |
| Width | 0.75126 | 9.20033e-38 |
| Curb-weight | 0.83441 | 2.18957e-53 |
| Engine-size | 0.87233 | 9.26549e-64 |
| Bore | 0.54315 | 8.04918e-17 |
| City-mpg | -0.68657 | 2.32113e-29 |
| Highway-mpg | -0.70469 | 1.74954e-31 |

<br/>
<br/>

- **Correlation in Categorical Variables**: By using boxplot, I illustrate the correlation between Price and Body-style first and Engine-location second, as shown in the figures below. From the plots we can conclude that the Engine-location is a good predictor for the Price, because its distrubation covers almost all price range, where Body-style categories have a notable overlap.

| <img width="350" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_4.png" alt="Correlation between Price and Body-style"/> | <img width="350" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_5.png" alt="Correlation between Price and Engine-location"/> |
|-|-|

<br/>
<br/>

- **ANOVA**: I calculate F-test score and P-value between Drive-wheels and Price. It shows high correlation as F-test score is 67.95. Also, P_value is near to 0, which means statistical significance between the two varibles. Additionally, Drive-wheels has 3 categories: fwd, rwd and 4wd where I calculate F-test score and P-value between fwd and rwd Price first, 4wd Price second and between rwd and 4rwd Price. Fwd vs. rwd has the higher correlation where 4wd vs. rwd has weak correlation and fwd vs. 4wd has no correlation.

<br/>
<br/>

## 3. Model Development
### Simple Linear Regression (SLR) and Multiple Linear Regression (MLR)
I used scikit-learn library to predict the price of cars in which I created two models. The first model is simple linear regression (SLR) that has two variables, the depentent variable (target) is the Price where the independent variable (predictor) is engine-size. Furthermore, the second model is multiple linear regression (MLR) and the depentent variable is also the Price, whereas the independent variables are Highway-mpg and normalized-losses.
<br/>
<br/>
### Evaluation of Simple Linear Regression (SLR) by visualization - Residual Plots
I created residuals plot to illustrate the distance between the price actual data point to the regression line. The residuals shows non-linear distribution, which means the SLR model is not appropriate for predicting the price. 

<img width="400" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_6.png" alt="Residual Plot between Price and highway-mpg"/>
<br/>

### Evaluation of Multiple Linear Regression (MLR) - Distribution Plots
I created distribution plot to illustrate the distribution distance between the price actual data point to the fitted data. The plot shows a significant overlap between the two distributions, which means MLR model could be an appropriate model to predict the price. 

<img width="400" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_7.png" alt=""/>

<br/>
<br/>

### Polynomial Regression
There is non-linear relationship between the price actual data point and the fitted regression line when highway_mpg is the independent variable as shown above in the evaluation of simple linear regression. Therefore, the soluation is to use a polynomial model to fit the data. I created 11 order polynomial model to predict the price of the cars.

<img width="400" src="https://github.com/zahraa-m/Python_Projects/blob/master/Plots/Figure_10.png" alt=""/>

<br/>

### Pipeline Method
I used pipeline method as a way to shorten the processing of the data as shown in the code-line 93 to 102 of [15-Model_Development.py](https://github.com/zahraa-m/Python_Projects/blob/master/15-Model_Development.py)

<br/>

###R-squared (R^2) and Mean Squared Error (MSE)
I Calculated the accuracy of the models by using R^2 and MSE. 
<br/>
<br/>

## 4. Model Evaluation


