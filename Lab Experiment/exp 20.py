
# Planets Database

planets = [
    ("Mercury", 1),
    ("Venus", 2),
    ("Earth", 3),
    ("Mars", 4),
    ("Jupiter", 5),
    ("Saturn", 6),
    ("Uranus", 7),
    ("Neptune", 8)
]

print("PLANETS DATABASE")
print("-------------------------")

for name, position in planets:
    print("Planet:", name)
    print("Position from Sun:", position)
    print("-------------------------")

# Search a planet
search = input("Enter planet name: ")

found = False

for name, position in planets:
    if name.lower() == search.lower():
        print("Planet:", name)
        print("Position:", position)
        found = True
        break

if not found:
    print("Planet not found")
