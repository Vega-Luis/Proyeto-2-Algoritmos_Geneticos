import cv2
target_name = 'target.jpg'
import random


def is_black(b):
    return b < 127
fitness = 0;
def get_aptitude(image_name):
    target_image = cv2.imread(target_name)
    actual_image = cv2.imread(image_name)
    step = 120
    image_size = 600
    samples = 60
    x_axis_ranges = [ [split, split + step] for split in range(0, image_size, step)]
    x_axis_reversed = x_axis_ranges[::-1]
    y_axis_ranges = [ sorted(element) for element in x_axis_reversed]
    sections_fit = []
    for row in range(5):
        for column in range(5):
            hits = 0
            for prove in range(samples):
                x_sample = random.randrange(x_axis_ranges[row][0], x_axis_ranges[row][1])
                y_sample = random.randrange(y_axis_ranges[column][0], y_axis_ranges[column][1])
                target_b, _, _ = target_image[x_sample, y_sample]
                actual_b, _, _ = actual_image[x_sample, y_sample]
                if is_black(target_b) and is_black(actual_b):
                    hits += 1
                if is_black(target_b) == False and is_black(actual_b) == False:
                    hits +=1
                if is_black(target_b) == False and is_black(actual_b):
                    hits -= 1
                if is_black(target_b) and is_black(actual_b) == False:
                    hits -= 1
            if hits == 0:
                sections_fit += [0]
            else:
                sections_fit += [hits/samples*100]
    fitness = 0
    for section in sections_fit:
        fitness += section * 0.04
    print(fitness)
    if fitness < 0:
        fitness = 0
    return fitness

#fitness('side.jpg')
