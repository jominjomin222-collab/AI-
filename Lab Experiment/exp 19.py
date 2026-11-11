
# Student-Teacher-Subject-Code Database

students = {
    101: ("Jomin", "Kumar", "Python"),
    102: ("Rahul", "Priya", "Java"),
    103: ("John", "Ravi", "AI")
}

print("STUDENT-TEACHER-SUBJECT DATABASE")
print("--------------------------------")

for sid, details in students.items():
    print("Student ID:", sid)
    print("Student Name:", details[0])
    print("Teacher Name:", details[1])
    print("Subject:", details[2])
    print("--------------------------------")

# Search student
n = int(input("Enter Student ID to search: "))

if n in students:
    print("Student Name:", students[n][0])
    print("Teacher Name:", students[n][1])
    print("Subject:", students[n][2])
else:
    print("Student not found")
