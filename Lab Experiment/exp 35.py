
# Decision Tree Classification

print("DECISION TREE CLASSIFICATION")

print("1. Sunny")
print("2. Rainy")
print("3. Cloudy")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    print("Weather: Sunny")
    print("Predicted Class: No")

elif choice == "2":
    print("Weather: Rainy")
    print("Predicted Class: Yes")

elif choice == "3":
    print("Weather: Cloudy")
    print("Predicted Class: Yes")

else:
    print("Invalid Choice")
