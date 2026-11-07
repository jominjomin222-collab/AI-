
# Map Coloring using CSP

# Define the regions and their neighbors
regions = ['A', 'B', 'C', 'D']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Check whether a color is valid
def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# CSP Backtracking algorithm
def map_coloring(assignment):
    if len(assignment) == len(regions):
        return assignment

    # Select an unassigned region
    region = next(r for r in regions if r not in assignment)

    # Try available colors
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color

            result = map_coloring(assignment)

            if result:
                return result

            # Backtracking
            del assignment[region]

    return None

# Solve the map coloring problem
solution = map_coloring({})

# Display the result
if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(region, ":", color)
else:
    print("No solution exists")

