
# Best First Search Algorithm

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
h = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

def best_first_search(start, goal):
    open_list = [start]
    visited = []

    while open_list:
        open_list.sort(key=lambda x: h[x])

        current = open_list.pop(0)

        if current in visited:
            continue

        print("Visiting:", current)
        visited.append(current)

        if current == goal:
            print("Goal Found:", goal)
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                open_list.append(neighbor)

    print("Goal not found")


# Main program
start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

if start in graph and goal in graph:
    best_first_search(start, goal)
else:
    print("Invalid node")
