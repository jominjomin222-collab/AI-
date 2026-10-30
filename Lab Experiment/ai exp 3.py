
from collections import deque

def water_jug(capacity1, capacity2, target):

    visited = set()
    queue = deque()

    queue.append((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        print("Jug1:", jug1, "Jug2:", jug2)

        if jug1 == target or jug2 == target:
            print("Target amount reached!")
            return

        # Fill Jug1
        queue.append((capacity1, jug2))

        # Fill Jug2
        queue.append((jug1, capacity2))

        # Empty Jug1
        queue.append((0, jug2))

        # Empty Jug2
        queue.append((jug1, 0))

        # Pour Jug1 into Jug2
        pour = min(jug1, capacity2 - jug2)
        queue.append((jug1 - pour, jug2 + pour))

        # Pour Jug2 into Jug1
        pour = min(jug2, capacity1 - jug1)
        queue.append((jug1 + pour, jug2 - pour))

    print("Solution not possible")

# Main program
water_jug(4, 3, 2)
