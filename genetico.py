import pygame, math
import random
import time
import numpy as np
from adaptation import *
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
screen.fill([255,255,255])
#there are 80 chars in this line this is the limit per line, ###################
population = []
individual_size = 96

def randRange(list):
    """
    Returns a random number from a given range by a two elements list
    """
    return random.randint(list[0], list[1])

def list_to_int(list):
    return int("".join(map(str, list)))

def bin_to_int(binary_dna):
    """Converts a binary list in to a decimal list
    
    Args:
        binary_dna: binary list that contains the individual dna
   
   Returns:
        A decimal list that contanins the individual dna
    """
    counter = 0
    grouped_dna = [''.join(str(element) for element in binary_dna[i:i + 4])
                        for i in range(0,len(binary_dna), 4)]
    decimal_dna = [str(int(element, 2)) for element in grouped_dna]
    return decimal_dna

def create_individual():
    """ This funtions creates an individual, each individual is binary list
        that reprensents the individual dna
    
    Returns:
        A binary list that contains de individual dna

    """
    decimal_dna = []
    branches = sorted([random.randint(0,4), random.randint(0,4)])
    fork_angle = sorted([random.randint(1,100), random.randint(1, 100)])
    base_length = sorted([random.randint(1, 300), random.randint(1,300)])
    individual = [random.randint(2, 9), format(random.randint(1, 150), '3d'), 
                    format(random.randint(1,99), '2d'), format(random.randint(1,99), '2d'),
                    format(random.randint(1,99), '2d'), branches[0], branches[1],
                    format(fork_angle[0], '3d'), format(fork_angle[1], '3d'),
                    format(base_length[0],'3d'), format(base_length[1], '3d')]
    
    for decimal_chromosome in individual:
        decimal_dna += ['0' if x== ' ' else x for x in str(decimal_chromosome) if x != '.'] 
    
    aux_dna = ["{0:b}".format(int(x)) if len("{0:b}".format(int(x))) == 4
                    else '0'*(4-len("{0:b}".format(int(x)))) + "{0:b}".format(int(x)) for x in decimal_dna]
   
    binary_dna = []
    for element in aux_dna:
        binary_dna += [x  for x in element]
    
    return binary_dna 

def generate_population(individuals):
    """Generates the initial population
    
    Args:
        individuals: Population individuals number
    """
    globals()['population']  = [create_individual() for individual in range(individuals)]
    

def translate_individual(individual):
    """ Make the chromosome of the individual understandable to be drawn 
    
    Args:
        individual: Individual to be drawn
    """
    individual = np.array(individual)
    depth = int(individual[0])
    diameter = int(list_to_int(individual[1:4]))
    decrement = float(list_to_int(individual[4:6]) / 100)
    base_decrement = float(list_to_int(individual[6:8]) / 100)
    branch_decrement = float(list_to_int(individual[8:10]) / 100)
    branches = [int(individual[10]), int(individual[11])]
    fork_angle = [int(list_to_int(individual[12:15])), int(list_to_int(individual[15:18]))]
    base_length = [int(list_to_int(individual[18:21])), int(list_to_int(individual[21:25]))]
    print(depth, diameter, decrement, base_decrement, branch_decrement, branches, fork_angle, base_length)
    draw_tree(300, 550, 270, branches, decrement, depth, diameter, fork_angle, base_length, base_decrement, branch_decrement)

def draw_tree(x1, y1, angle, branches, decrement, depth, diameter, fork_angle, base_len, base_decrement, branch_decrement):
    """
    draw a tree from the chromosomes
    """
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * base_decrement * randRange(base_len)) + 1
        y2 = y1 + int(math.sin(math.radians(angle)) * base_decrement * randRange(base_len)) + 1
        pygame.draw.line(screen, (0,0,0), (x1, y1), (x2, y2), int(diameter*decrement) + 1)

        aux_branches = random.randint(branches[0], branches[1])
 
        draw_tree(x2, y2, angle, branches, decrement**2, depth - 1, int(diameter * decrement), fork_angle, base_len, base_decrement**2, branch_decrement)
        for branch in range(1, aux_branches // 2 + 1):
            draw_tree(x2, y2, angle + random.randint(fork_angle[0],fork_angle[1])*branch, 
                    branches, decrement**2, depth - 1,diameter, fork_angle, base_len, branch_decrement, branch_decrement**2)
            draw_tree(x2, y2, angle - random.randint(fork_angle[0],fork_angle[1])*branch, 
                    branches, decrement**2, depth - 1, diameter, fork_angle, base_len, branch_decrement, branch_decrement**2)
        if aux_branches % 2 == 1:
            if random.randint(0,1) == 0:
                draw_tree(x2, y2, angle - random.randint(fork_angle[0],fork_angle[1])*(aux_branches // 2 + 1), 
                        branches, decrement**2, depth - 1, diameter,fork_angle, base_len, branch_decrement, branch_decrement**2)
            else:
                draw_tree(x2, y2, angle + random.randint(fork_angle[0],fork_angle[1])*(aux_branches // 2 + 1), 
                        branches, decrement**2, depth - 1, diameter, fork_angle, base_len, branch_decrement, branch_decrement**2)
def input(event):
    if event.type == pygame.QUIT:
        exit(0)

def main():
    generations = 100 
    initial_population = 20
    generate_population(initial_population)
    
    for i in range(generations):
        fitness = []
        for individual in population:
            translate_individual(bin_to_int(individual))
            pygame.image.save(window, "output.jpg")
            fit("output")
            pygame.display.flip()
            screen.fill([255,255,255])
        fitness = np.array(get_fitness())
        fitness = fitness/fitness.sum()
        print(fitness, "hos")
        offspring = []
        for i in range(len(population)//2):
            parents = np.random.choice(len(population), 2,  p = fitness)
            split_point = np.random.randint(individual_size)
            offspring += [population[parents[0]][:split_point] + population[parents[1]][split_point:]]
            offspring += [population[parents[1]][:split_point] + population[parents[0]][split_point:]]
        globals()['population'] = offspring

main()
while True:
    input(pygame.event.wait())
