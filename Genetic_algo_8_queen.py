import random

def fitness(board):
    collisions = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                collisions += 1
    return 1 / (collisions + 1)

def random_individual(size):
    return [random.randint(0, size - 1) for _ in range(size)]

def crossover(parent1, parent2):
    pivot = random.randint(1, len(parent1) - 1)
    child1 = parent1[:pivot] + parent2[pivot:]
    child2 = parent2[:pivot] + parent1[pivot:]
    return child1, child2

def mutate(individual):
    index = random.randint(0, len(individual) - 1)
    new_gene = random.randint(0, len(individual) - 1)
    individual[index] = new_gene
    return individual

def genetic_algorithm(population_size, board_size, generations):
    population = [random_individual(board_size) for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        new_population = []

        for i in range(0, population_size, 2):
            parent1, parent2 = population[i], population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])

        population = new_population

    best_solution = max(population, key=lambda x: fitness(x))
    return best_solution

# Example usage
if __name__ == "__main__":
    population_size = 100
    board_size = 8
    generations = 1000

    solution = genetic_algorithm(population_size, board_size, generations)
    print("Best solution:", solution)
