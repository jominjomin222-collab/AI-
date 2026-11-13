
# Principal Component Analysis (PCA)

import math

print("PCA DIMENSIONALITY REDUCTION")

# Dataset
data = [
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7]
]

n = len(data)

# Find mean
mean1 = sum(row[0] for row in data) / n
mean2 = sum(row[1] for row in data) / n

# Center the data
x = []
y = []

for row in data:
    x.append(row[0] - mean1)
    y.append(row[1] - mean2)

# Calculate covariance
a = sum(i * i for i in x) / (n - 1)
b = sum(x[i] * y[i] for i in range(n)) / (n - 1)
c = sum(i * i for i in y) / (n - 1)

# Calculate principal component
angle = 0.5 * math.atan2(2 * b, a - c)

v1 = math.cos(angle)
v2 = math.sin(angle)

print("Principal Component:")
print(round(v1, 3), round(v2, 3))

# Reduce dimensions
print("Reduced Data:")

for i in range(n):
    result = x[i] * v1 + y[i] * v2
    print(round(result, 3))
