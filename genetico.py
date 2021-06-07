import pygame, math
import random

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
screen.fill([255,255,255])

def randRange(list):
    """
    Returns a random number from a given range by a two elements list
    """
    return random.randint(list[0], list[1])

def drawTree(x1, y1, angle, branches, decrement, depth, diameter, fork_angle, base_len, base_decrement, branch_decrement):
    """
    draw a tree from the chromosomes
    """
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * base_decrement * randRange(base_len))
        y2 = y1 + int(math.sin(math.radians(angle)) * base_decrement * randRange(base_len))
        pygame.draw.line(screen, (0,0,0), (x1, y1), (x2, y2), int(diameter*decrement) + 1)

        aux_branches = random.randint(branches_number[0], branches_number[1])

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

#drawTree(x1, y1, angle, depth, base_len, fork_angle, diameter):
for i in range(0, 101):
    x1 = 300
    y1 = 550

    angle = 270
    depth = 7
    diameter = 50
    decrement = 0.9999999999
    decrement = 0.9999999999
    base_decrement = 0.85
    branch_decrement = 0.7
    branches_number = [1,3]
    fork_angle = [20,40]
    base_length = [20,200] 
    drawTree(x1, y1, angle, branches_number, decrement, depth, diameter, fork_angle, base_length, base_decrement, branch_decrement)

    pygame.display.flip()
    screen.fill([255,255,255])

while True:
    input(pygame.event.wait())
