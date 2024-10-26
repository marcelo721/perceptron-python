# Perceptron Weight Adjustment

This project implements a basic Perceptron model in Python, focusing on understanding how weights are adjusted during training. The model includes functions for training using the AND, OR, and XOR operators, allowing users to experiment with different logical functions.

## Project Overview

A Perceptron is a simple type of neural network used for binary classification tasks. This project demonstrates how a Perceptron learns by adjusting its weights based on training data and a learning rate.

## Features

- **Logical Operators**: Test the model using AND, OR, and XOR operators.
- **Training Function**: Adjusts weights based on training data until the network reaches zero errors.
- **Step Activation Function**: Outputs a binary result (0 or 1) based on a threshold.

## Files

- **`weight_adjustment.py`**: Contains the code for the Perceptron model, including weight adjustment and training functions.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/marcelo721/perceptron-python.git
    ```
2. Run the code:
    ```bash
    python weight_adjustment.py
    ```

## Example Output

The program will print the updated weights after each iteration and the final result of the trained Perceptron for each input.

## Requirements

- Python 3.x
- NumPy library

Install NumPy with:
```bash
pip install numpy
