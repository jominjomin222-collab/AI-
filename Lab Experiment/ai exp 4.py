
from itertools import permutations

def solve_cryptarithmetic():
    letters = 'SENDMORY'

    for perm in permutations('0123456789', len(letters)):
        values = dict(zip(letters, perm))

        # First letters cannot be zero
        if values['S'] == '0' or values['M'] == '0':
            continue

        SEND = int(''.join(values[c] for c in 'SEND'))
        MORE = int(''.join(values[c] for c in 'MORE'))
        MONEY = int(''.join(values[c] for c in 'MONEY'))

        if SEND + MORE == MONEY:
            print("Solution Found!")
            print("SEND =", SEND)
            print("MORE =", MORE)
            print("MONEY =", MONEY)
            return

    print("No solution found")

# Main program
solve_cryptarithmetic()
