
import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0),
             (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors

def solve(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

solution = solve(start)

if solution:
    print("Solution Found!")
    print("Number of moves:", len(solution) - 1)

    for step in solution:
        display(step)
else:
    print("No solution exists.")
