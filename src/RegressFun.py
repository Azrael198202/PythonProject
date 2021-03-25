# Regress Function
# the relationship between input and output 

# sum of squares of different
# ordinary leasts squares OLS
import sys
import numpy as np

#filename = sys.argv[1]
filename = 'data_singlevar.txt'

X = []
Y = []

with open(filename, 'r') as f :
    for line in f.readlines() :
        xt, yt = [float(i) for i in line.split(',')]
        X.append(xt)
        Y.append(yt)

num_training = int(0.8 * len(X))
num_test = len(X) - num_training

# training data
X_train = np.array(X[:num_training]).reshape((num_training, 1))
Y_train = np.array(X[:num_training])

# test data
X_test = np.array(X[num_training:]).reshape((num_test,1))
Y_test = np.array(X[:num_training : ])

from sklearn import linear_model

# create line regressor
linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(X_train, Y_train)


import matplotlib.pyplot as plt

y_trian_pred = linear_regressor.predict(X_train)
plt.figure()
plt.scatter(X_train, Y_train, color='green')
plt.plot(X_train, y_trian_pred, color='black', linewidth = 1)
plt.title('Training data')

y_test_pred = linear_regressor.predict(X_test)
#plt.scatter(X_test, Y_test, color='green')
#plt.plot(X_test, y_test_pred, color='black', linewidth=4)
plt.title('Test data')
plt.show()