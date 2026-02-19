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

POPULATION_SIZE = 12

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


def evolve_population(population):
    new_population = []

    # 1. Calcular fitness de todos
    for individuo in population:
        calculate_fitness(individuo)

    # 2. Ordenar população pelo melhor fitness (maior primeiro)
    population.sort(key=lambda ind: ind.fitness, reverse=True)

    # 3. ELITISMO: preservar o melhor
    elite = population[0]
    new_population.append(elite)

    # 4. Gerar o resto da população
    while len(new_population) < POPULATION_SIZE:
        pai1 = select_parent(population)
        pai2 = select_parent(population)

        filho = crossover(pai1, pai2)
       # mutate(filho)

        new_population.append(filho)

    return new_population




# ===============================
# VISUALIZAÇÃO (PYGAME)
# ===============================

import pygame
import sys

# inicializa o pygame
pygame.init()

# cria a janela
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Camouflage - Teste")

# controle de FPS
clock = pygame.time.Clock()

# antes do loop
population = create_population()
last_evolution_time = 0
EVOLUTION_INTERVAL = 1000  # 1 segundo
colunas = 8
TAMANHO = 50


# ===============================
# LOOP PRINCIPAL
# ===============================


running = True
while running:
    clock.tick(60)

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TEMPO ATUAL
    current_time = pygame.time.get_ticks()

    # EVOLUÇÃO (lógica)
    if current_time - last_evolution_time > EVOLUTION_INTERVAL:
        population = evolve_population(population)
        last_evolution_time = current_time

    # DESENHO
    screen.fill(BACKGROUND_COLOR)

    for i, individuo in enumerate(population):
        coluna = i % colunas
        linha = i // colunas

        x = coluna * TAMANHO
        y = linha * TAMANHO

        pygame.draw.rect(
            screen,
            (individuo.r, individuo.g, individuo.b),
            (x, y, 40, 40)
        )


    pygame.display.flip()

pygame.quit()
sys.exit()



