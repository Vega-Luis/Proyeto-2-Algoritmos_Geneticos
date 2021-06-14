import pygame, math
import random
import time
import numpy as np
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
screen.fill([255,255,255])
#there are 80 chars in this line this is the limit per line, ###################
population = []
fitness = []
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
    branches = sorted([random.randint(0,9), random.randint(0,9)])
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
    print(individual, "indi")
    individual = np.array(individual)
    depth = individual[0]
    diameter = list_to_int(individual[1:4])
    decrement = list_to_int(individual[4:6]) / 100
    base_decrement = list_to_int(individual[6:8]) / 100
    branch_decrement = list_to_int(individual[8:10]) / 100
    branches = [individual[10], individual[11]]
    fork_angle = [list_to_int(individual[12:15]), list_to_int(individual[15:18])]
    base_length = [list_to_int(individual[18:21]), list_to_int(individual[21:25])]
    print(depth,diameter, decrement, base_decrement, branch_decrement, branches, fork_angle, base_length)

def draw_tree(x1, y1, angle, branches, decrement, depth, diameter, fork_angle, base_len, base_decrement, branch_decrement):
    """
    draw a tree from the chromosomes
    """
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * base_decrement * randRange(base_len)) + 1
        y2 = y1 + int(math.sin(math.radians(angle)) * base_decrement * randRange(base_len)) + 1
        pygame.draw.line(screen, (0,0,0), (x1, y1), (x2, y2), int(diameter*decrement) + 1)

        aux_branches = random.randint(branches[0], branches[1])
 
        drawTree(x2, y2, angle, branches, decrement**2, depth - 1, int(diameter * decrement), fork_angle, base_len, base_decrement**2, branch_decrement)
        for branch in range(1, aux_branches // 2 + 1):
            drawTree(x2, y2, angle + random.randint(fork_angle[0],fork_angle[1])*branch, 
                    branches, decrement**2, depth - 1,diameter, fork_angle, base_len, branch_decrement, branch_decrement**2)
            drawTree(x2, y2, angle - random.randint(fork_angle[0],fork_angle[1])*branch, 
                    branches, decrement**2, depth - 1, diameter, fork_angle, base_len, branch_decrement, branch_decrement**2)
        if aux_branches % 2 == 1:
            if random.randint(0,1) == 0:
                drawTree(x2, y2, angle - random.randint(fork_angle[0],fork_angle[1])*(aux_branches // 2 + 1), 
                        branches, decrement**2, depth - 1, diameter,fork_angle, base_len, branch_decrement, branch_decrement**2)
            else:
                drawTree(x2, y2, angle + random.randint(fork_angle[0],fork_angle[1])*(aux_branches // 2 + 1), 
                        branches, decrement**2, depth - 1, diameter, fork_angle, base_len, branch_decrement, branch_decrement**2)
def input(event):
    if event.type == pygame.QUIT:
        exit(0)

def main():
    generations = 100
    initial_population = 100
    
    generate_population(initial_population)
    print(population)
    
    for _ in range(generations):
        #print(translate_individual(bin_to_int(population[0])))
        #translate_individual(population[0])
        #fitnes
        #cruce
        #mutacion
        depth = 6
        diameter = 29 
        decrement = 0.99
        base_decrement = 0.99
        branch_decrement = 0.6
        branches = [2,4]
        fork_angle = [80,90]
        base_length = [100,100] 

        #draw_tree(300, 550, 270, branches, decrement, depth, diameter, fork_angle, base_length, base_decrement, branch_decrement)
        pygame.display.flip()
        screen.fill([255,255,255])
main()
while True:
    input(pygame.event.wait())
