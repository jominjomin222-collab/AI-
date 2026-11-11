
# Fruit and Color Database

fruits = [
    ("apple", "red"),
    ("banana", "yellow"),
    ("orange", "orange"),
    ("grapes", "green"),
    ("mango", "yellow"),
    ("guava", "green"),
    ("cherry", "red")
]

print("FRUIT AND COLOR DATABASE")
print("----------------------------")

# Display all fruits and colors
for fruit, color in fruits:
    print("Fruit:", fruit, "Color:", color)

# Search fruits by color
search = input("\nEnter color to search: ").lower()

found = False

print("Fruits with", search, "color:")

for fruit, color in fruits:
    if color == search:
        print(fruit)
        found = True

if not found:
    print("No fruit found")

