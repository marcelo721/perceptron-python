import numpy as np

# Sigmoid function implementation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(sig):
    return sig * (1 - sig)


# Input and output data
inputs = np.array([[0, 0],
                   [0, 1],
                   [1, 0],
                   [1, 1]])

outputs = np.array([[0], [1], [1], [0]])

# Initializing weights with random values
weights0 = 2 * np.random.random((2, 3)) - 1
weights1 = 2 * np.random.random((3, 1)) - 1

# Training parameters
training_time = 1000
learning_rate = 0.6
momentum = 1

for j in range(training_time):
    # Forward propagation
    input_layer = inputs
    hidden_input = np.dot(input_layer, weights0)
    hidden_layer = sigmoid(hidden_input)

    output_input = np.dot(hidden_layer, weights1)
    output_layer = sigmoid(output_input)

    # Calculate error
    output_error = outputs - output_layer
    mean_absolute_error = np.mean(abs(output_error))
    print("Error:")
    print(mean_absolute_error)

    # Backpropagation
    output_derivative = sigmoid_derivative(output_layer)
    output_delta = output_error * output_derivative

    weights1_transpose = weights1.T
    hidden_error = output_delta.dot(weights1_transpose)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_layer)

    hidden_layer_transpose = hidden_layer.T
    weights1_update = hidden_layer_transpose.dot(output_delta)
    weights1 = (weights1 * momentum) + (weights1_update * learning_rate)

    input_layer_transpose = input_layer.T
    weights0_update = input_layer_transpose.dot(hidden_delta)
    weights0 = (weights0 * momentum) + (weights0_update * learning_rate)

    print(output_layer)
