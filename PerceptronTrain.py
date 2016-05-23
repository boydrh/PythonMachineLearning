import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', headers=None)
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df.tail()
import matplotlib.pyplot as plt
import numpy as np
y = df.iloc[0:100, 4].values
y = np.where( y== 'Iris-setosa', -1,1)
y[0]
X = df.iloc[0:100, [0,2]].values
plt.scatter(X[:50, 0], X[:50,1], color = 'red', marker = 'o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100,1], color = 'blue', marker = 'x', label='versicolor')
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc='upper left')
plt.show()
import Percepton
import Perceptron
ppn = Perceptron(eta=0.1, n_iter=10)
ppn = Perceptron.Perceptron(eta=0.1, n_iter=10)
ppn.fit(X,y)
plt.plot(range(1, len(ppn.errors_)+1),ppn.errors_,marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of Misclassifications')
plt.show()

import readline
readline.write_history_file("PerceptronTrain.py")
