import numpy as np

# Feature vector (e.g., age, height, weight)
x = np.array([25, 175, 70])

# Dataset matrix (rows = samples, columns = features)
X = np.array([[25, 175, 70],
              [30, 180, 80],
              [22, 165, 60]])

print("Feature vector:", x)
print("Dataset matrix:\n", X)
# Input features
X = np.array([[0.5, 1.2],
              [1.0, 0.8]])

# Weights
W = np.array([[0.4, 0.7],
              [0.3, 0.9]])

# Bias
b = np.array([0.1, 0.2])

# Forward pass: XW + b
output = np.dot(X, W) + b
print("Neural network layer output:\n", output)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

z = np.array([-1, 0, 2])
print("Sigmoid:", sigmoid(z))
print("ReLU:", relu(z))
# True labels
y_true = np.array([1, 0, 1])

# Predicted probabilities
y_pred = np.array([0.9, 0.2, 0.8])

# Mean Squared Error (MSE)
mse = np.mean((y_true - y_pred) ** 2)

# Cross-Entropy Loss
epsilon = 1e-9  # to avoid log(0)
cross_entropy = -np.mean(y_true * np.log(y_pred + epsilon) + (1 - y_true) * np.log(1 - y_pred + epsilon))

print("MSE:", mse)
print("Cross-Entropy Loss:", cross_entropy)
def f(x):
    return x**2 + 3*x + 2

# Numerical gradient at x=2
x = 2.0
h = 1e-5
grad = (f(x + h) - f(x - h)) / (2*h)

print("Gradient at x=2:", grad)
