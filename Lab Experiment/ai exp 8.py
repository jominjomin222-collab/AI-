
def dfs(graph, start, visited=None):

    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=" ")
        visited.add(start)

        for neighbour in graph[start]:
            dfs(graph, neighbour, visited)


# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Main program
print("DFS Traversal:")
dfs(graph, 'A')
