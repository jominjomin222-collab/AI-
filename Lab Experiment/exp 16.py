
# Feed Forward Neural Network

import math

# Input values
inputs = [0.5, 0.2]

# Weights and biases
weights1 = [[0.4, 0.3],
            [0.2, 0.5]]

bias1 = [0.1, 0.1]

weights2 = [0.6, 0.4]
bias2 = 0.2

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Hidden layer
hidden = []

for j in range(2):
    total = bias1[j]

    for i in range(2):
        total += inputs[i] * weights1[i][j]

    hidden.append(sigmoid(total))

# Output layer
output = bias2

for i in range(2):
    output += hidden[i] * weights2[i]

final_output = sigmoid(output)

# Display result
print("Feed Forward Neural Network")
print("Input Layer:", inputs)
print("Hidden Layer:", hidden)
print("Output Layer:", final_output)
