import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2, -1, 0, 1, 2])

# sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# tanh
def tanH(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

# ReLU
def reLU(x):
    return np.maximum(0, x)

# Leaky ReLU
def leaky_reLU(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Softmax
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)

activation = {
    "Sigmoid": sigmoid,
    "Tanh": tanH,
    "ReLU": reLU,
    "Leaky ReLU": leaky_reLU,
    "Softmax": softmax
}

plt.figure(figsize=(10, 8))

for i, (name, func) in enumerate(activation.items(), 1):
    plt.subplot(3, 2, i)
    y = func(x)
    plt.plot(x, y)
    plt.title(name)
    plt.grid(True)

plt.tight_layout()
plt.show()