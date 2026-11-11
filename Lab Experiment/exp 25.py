
# Monkey Banana Problem

monkey = "door"
box = "window"
banana = "middle"

print("MONKEY BANANA PROBLEM")
print("----------------------------")

print("Initial Position:")
print("Monkey:", monkey)
print("Box:", box)
print("Banana:", banana)

# Step 1: Monkey walks to the box
monkey = box
print("\nStep 1: Monkey walks to the box")

# Step 2: Monkey pushes the box to middle
box = "middle"
monkey = "middle"
print("Step 2: Monkey pushes the box to middle")

# Step 3: Monkey climbs the box
print("Step 3: Monkey climbs the box")

# Step 4: Monkey grabs the banana
print("Step 4: Monkey grabs the banana")

print("\nResult: Monkey got the banana!")
