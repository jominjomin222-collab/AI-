
print("MEDICAL DIAGNOSIS SYSTEM")
print("------------------------")

fever = input("Enter fever (yes/no): ")
cough = input("Enter cough (yes/no): ")
cold = input("Enter cold (yes/no): ")

if fever == "yes" and cough == "yes":
    print("Possible Disease: Flu-like illness")

elif cold == "yes":
    print("Possible Disease: Common Cold")

elif fever == "yes":
    print("Possible Condition: Fever")

else:
    print("No matching disease found")

print("Consult a doctor for proper diagnosis.")
