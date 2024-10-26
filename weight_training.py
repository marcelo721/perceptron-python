import numpy as np

# Test AND operator
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([0, 0, 0, 1])

# Test OR operator
# inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# outputs = np.array([0, 1, 1, 1])

# Test XOR operator
#inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#outputs = np.array([0, 1, 1, 0])

weights = np.array([0.0, 0.0])
learningRate = 0.1

def stepFunction(sum):
    if sum >= 1:
        return 1
    else:
        return 0

def calculateSum(record):
    s = record.dot(weights)
    return stepFunction(s)

def train():
    totalError = 1
    while(totalError != 0):
        totalError = 0
        for i in range(len(outputs)):
            calculatedOutput = calculateSum(np.asarray(inputs[i]))
            error = abs(outputs[i] - calculatedOutput)
            totalError += error
            for j in range(len(weights)):
                weights[j] = weights[j] + (learningRate * inputs[i][j] * error)
                print('updated weight: ' + str(weights[j]))
            print('total errors = ' + str(totalError))

train()

print("Neural network trained")
print(calculateSum(inputs[0]))
print(calculateSum(inputs[1]))
print(calculateSum(inputs[2]))
print(calculateSum(inputs[3]))
