
# Towers of Hanoi

def hanoi(n, source, destination, auxiliary):

    if n == 1:
        print("Move disk from", source, "to", destination)
        return

    hanoi(n - 1, source, auxiliary, destination)

    print("Move disk from", source, "to", destination)

    hanoi(n - 1, auxiliary, destination, source)


# Main program

n = int(input("Enter number of disks: "))

if n > 0:
    hanoi(n, 'A', 'C', 'B')
else:
    print("Enter a positive number")
