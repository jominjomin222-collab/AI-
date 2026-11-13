
# K-Nearest Neighbors Classification

data = [
    [1, 2, "A"],
    [2, 3, "A"],
    [3, 3, "A"],
    [6, 7, "B"],
    [7, 8, "B"],
    [8, 8, "B"]
]

# Get input
x = float(input("Enter X value: "))
y = float(input("Enter Y value: "))

k = 3
dist = []

# Find distances
for p in data:
    d = ((p[0] - x) ** 2 +
         (p[1] - y) ** 2) ** 0.5

    dist.append([d, p[2]])

# Sort distances
dist.sort()

# Count nearest classes
a = 0
b = 0

for i in range(k):
    if dist[i][1] == "A":
        a = a + 1
    else:
        b = b + 1

# Classification
if a > b:
    print("Predicted Class: A")
elif b > a:
    print("Predicted Class: B")
else:
    print("Tie between classes")

print("K Nearest Neighbors:")
for i in range(k):
    print(dist[i])
