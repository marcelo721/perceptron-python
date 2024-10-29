import numpy as np

#sigmoid function implementation
def sigmoid(sum):
    return 1 / (1 + np.exp(-sum))