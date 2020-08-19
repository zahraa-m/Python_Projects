import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

URL = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/module_5_auto.csv'
df = pd.read_csv(URL)
df.to_csv('module_5_auto.csv')
df = df._get_numeric_data()


def distplot(rfunction, bunction, rname, bname, title):
    ax1 = sns.distplot(rfunction, hist=False, color="r", label=rname)
    ax2 = sns.distplot(bunction, hist=False, color="b", label=bname, ax=ax1)
    plt.title(title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')
    plt.show()
    plt.close()


def PollyPlot(xtrain, xtest, y_train, y_test, lr, poly_transform):
    xmax = max([xtrain.values.max(), xtest.values.max()])
    xmin = min([xtrain.values.min(), xtest.values.min()])
    x = np.arange(xmin, xmax, 0.1)
    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()


# Split the data for training and testing
y_data = df['price']
x_data = df.drop('price', axis=1)

from sklearn.model_selection import train_test_split
x_train_1, x_test_1, y_train_1, y_test_1 = train_test_split(x_data, y_data, test_size=0.30, random_state=0)
print(x_test_1.shape[0])
print(x_train_1.shape[0])



