import random

distances = [
    [0, 10, 20, 15, 25],  
    [10, 0, 30, 5, 18],  
    [20, 30, 0, 12, 35],  
    [15, 5, 12, 0, 10],  
    [25, 18, 35, 10, 0]  
]

NUM_BEES = 10
ITERATIONS = 100
MUTATION_RATE = 0.8

def generate_random_path(num_locations):
    path = list(range(1, num_locations))
    random.shuffle(path)
    return [0] + path + [0]

def calculate_total_distance(path):
    total_distance = 0
    for i in range(len(path)-1):
        total_distance+=distances[path[i]][path[i+1]]
    return total_distance

def mutate(path):
    if random.random() < MUTATION_RATE:
        new_path = path[:]
        i, j = random.sample(range(1, len(path)-1), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        return new_path
    return path

def optimize_path():
    bees = [generate_random_path(len(distances)) for _ in range (NUM_BEES)]

    for _ in range (ITERATIONS):
        distances_list = [(bee, calculate_total_distance(bee)) for bee in bees]

        distances_list.sort(key = lambda x: x[1])
        best_bees = [x[0] for x in distances_list[:NUM_BEES//2]]

        new_bees = best_bees[:]
        for bee in best_bees:
            new_bees.append(mutate(bee))

        bees = new_bees

    best_path = min(bees, key = calculate_total_distance)
    best_distance = calculate_total_distance(best_path)
    return best_path, best_distance

best_path, best_distance = optimize_path()
print("Best Path:", best_path)
print("Best Distance:", best_distance)
