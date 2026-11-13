
# Genetic Algorithm for Optimization

import random

# Fitness function
def fitness(x):
    return x * x

# Create population
population = [2, 5, 8, 10, 15, 20]

print("Initial Population:", population)

# Genetic algorithm
for generation in range(5):

    # Selection
    population.sort(reverse=True)

    parent1 = population[0]
    parent2 = population[1]

    # Crossover
    child = (parent1 + parent2) // 2

    # Mutation
    if random.randint(1, 10) == 1:
        child = random.randint(0, 31)

    # Replace weakest individual
    population[-1] = child

    print("Generation", generation + 1)
    print("Population:", population)

# Best solution
best = max(population)

print("Best Solution:", best)
print("Maximum Fitness:", fitness(best))
