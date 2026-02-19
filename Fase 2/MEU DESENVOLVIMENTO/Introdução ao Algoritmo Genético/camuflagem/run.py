# ===============================
# CONFIGURAÇÕES
# ===============================

# Cor do ambiente (fundo)
BACKGROUND_COLOR = (120, 200, 150)  # exemplo


# ===============================
# CLASSE INDIVIDUAL
# ===============================
import random

class Individual:
    def __init__(self):
        # Gene = cor RGB
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

        # Fitness começa zerado
        self.fitness = 0



# ===============================
# FUNÇÕES DO ALGORITMO GENÉTICO
# ===============================

POPULATION_SIZE = 40

def create_population():
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(Individual())
    return population


def calculate_fitness(individual):
    # Erro quadrático por canal
    error_r = (individual.r - BACKGROUND_COLOR[0]) ** 2
    error_g = (individual.g - BACKGROUND_COLOR[1]) ** 2
    error_b = (individual.b - BACKGROUND_COLOR[2]) ** 2

    error = error_r + error_g + error_b

    # Converter erro em fitness (quanto menor o erro, maior o fitness)
    individual.fitness = 1 / (error + 1)

def select_parent(population):
    total_fitness = sum(ind.fitness for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0

    for ind in population:
        current += ind.fitness
        if current >= pick:
            return ind
        
def crossover(parent1, parent2):
    child = Individual()

    # Para cada canal, escolhe aleatoriamente de qual pai vem o gene
    child.r = random.choice([parent1.r, parent2.r])
    child.g = random.choice([parent1.g, parent2.g])
    child.b = random.choice([parent1.b, parent2.b])

    return child

MUTATION_RATE = 0.1  # 10%

def mutate(individual):
    if random.random() < MUTATION_RATE:
        individual.r = random.randint(0, 255)

    if random.random() < MUTATION_RATE:
        individual.g = random.randint(0, 255)

    if random.random() < MUTATION_RATE:
        individual.b = random.randint(0, 255)



# ===============================
# VISUALIZAÇÃO (PYGAME)
# ===============================


# ===============================
# LOOP PRINCIPAL
# ===============================
