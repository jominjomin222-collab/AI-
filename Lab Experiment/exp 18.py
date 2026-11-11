
# Database with Name and Date of Birth

database = [
    ("John", "12-05-2000"),
    ("James", "20-08-2001"),
    ("Rahul", "15-03-2002"),
    ("Jomin", "25-11-2003")
]

print("Name\tDOB")
print("---------------------")

for name, dob in database:
    print(name, "\t", dob)

# Search for a person
search = input("\nEnter name to search: ")

found = False

for name, dob in database:
    if name.lower() == search.lower():
        print("Name:", name)
        print("DOB:", dob)
        found = True
        break

if not found:
    print("Record not found")
