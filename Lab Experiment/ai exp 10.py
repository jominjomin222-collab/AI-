
import heapq

def astar(graph, heuristic, start, goal):

    queue = []
    heapq.heappush(queue, (heuristic[start], start))

    cost = {start: 0}
    parent = {start: None}

    while queue:
        f, current = heapq.heappop(queue)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            print("Shortest Path:", path)
            print("Total Cost:", cost[goal])
            return

        for neighbor, weight in graph[current]:

            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]

                heapq.heappush(queue, (priority, neighbor))
                parent[neighbor] = current

    print("No path found")


# Graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 3)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'G': 0
}

# Main program
astar(graph, heuristic, 'A', 'G')
