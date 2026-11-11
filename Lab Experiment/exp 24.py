
# Diet Suggestion System Based on Disease

diet = {
    "diabetes": "Balanced meals with vegetables and whole grains",
    "fever": "Light meals, soup and adequate fluids",
    "obesity": "Balanced meals with vegetables, fruits and whole grains",
    "anemia": "Iron-rich foods such as spinach, beans and lentils"
}

print("DIET SUGGESTION SYSTEM")
print("-----------------------------")

disease = input("Enter disease name: ").lower()

if disease in diet:
    print("Disease:", disease)
    print("Suggested Diet:", diet[disease])
else:
    print("Disease not found in database.")
