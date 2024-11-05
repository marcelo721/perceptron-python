from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()
inputs = iris.data
outputs = iris.target

neuralNetwork = MLPClassifier(verbose=True, max_iter= 10000)
neuralNetwork.fit(inputs, outputs)