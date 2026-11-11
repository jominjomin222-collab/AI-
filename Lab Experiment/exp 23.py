
# Family Tree Program

family = {
    "john": ["robert"],
    "mary": ["robert"],
    "robert": ["david", "susan"],
    "lisa": ["david", "susan"],
    "david": ["james"]
}

# Find children
def children(name):
    return family.get(name, [])

# Find parents
def parents(name):
    result = []
    for parent, child_list in family.items():
        if name in child_list:
            result.append(parent)
    return result

# Main program
print("FAMILY TREE")
print("1. Find Children")
print("2. Find Parents")

choice = int(input("Enter your choice: "))
name = input("Enter name: ").lower()

if choice == 1:
    result = children(name)
    print("Children:", result if result else "No records found")

elif choice == 2:
    result = parents(name)
    print("Parents:", result if result else "No records found")

else:
    print("Invalid choice")
