
# Bird Flying Database

birds = {
    "parrot": True,
    "pigeon": True,
    "crow": True,
    "sparrow": True,
    "ostrich": False,
    "penguin": False,
    "kiwi": False
}

# Check whether a bird can fly

bird = input("Enter bird name: ").lower()

if bird in birds:
    if birds[bird]:
        print(bird, "can fly.")
    else:
        print(bird, "cannot fly.")
else:
    print("Bird not found in database.")

