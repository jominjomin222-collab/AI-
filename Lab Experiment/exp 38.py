
# Support Vector Machine
# Binary Classification

print("SVM BINARY CLASSIFICATION")

# Training data
x = [1, 2, 3, 6, 7, 8]
y = [2, 3, 2, 7, 8, 7]

labels = [0, 0, 0, 1, 1, 1]

# Input values
a = float(input("Enter X value: "))
b = float(input("Enter Y value: "))

# Calculate distances
d0 = 0
d1 = 0
c0 = 0
c1 = 0

for i in range(6):

    distance = ((x[i] - a) ** 2 +
                (y[i] - b) ** 2) ** 0.5

    if labels[i] == 0:
        d0 = d0 + distance
        c0 = c0 + 1
    else:
        d1 = d1 + distance
        c1 = c1 + 1

# Average distance
d0 = d0 / c0
d1 = d1 / c1

# Classification
if d0 < d1:
    print("Predicted Class: 0")
else:
    print("Predicted Class: 1")

print("Class 0 Distance:", round(d0, 2))
print("Class 1 Distance:", round(d1, 2))
