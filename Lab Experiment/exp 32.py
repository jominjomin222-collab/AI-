
# Linear Regression Program

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)

sum_x = sum(x)
sum_y = sum(y)

sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]

# Calculate slope
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

# Calculate intercept
a = (sum_y - b * sum_x) / n

print("Linear Regression")
print("Slope =", round(b, 2))
print("Intercept =", round(a, 2))

# Predict output
value = float(input("Enter X value: "))

result = a + b * value

print("Predicted value =", round(result, 2))
