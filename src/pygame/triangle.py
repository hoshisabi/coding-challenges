import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("triangle thing")
pygame.display.update()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

colors = [RED, WHITE, GREEN]

clock = pygame.time.Clock()
i = 0

start_points = [[random.randrange(1, 200), random.randrange(200, 400)],
                [random.randrange(300, 500), random.randrange(1, 100)],
                [random.randrange(600, 800), random.randrange(400, 600)]]


def random_color():
    return random.choice(colors)


def draw_point(p):
    pygame.draw.circle(screen, random_color(), p, 1)


def new_point(p):
    start = random.choice(start_points)
    return [(start[0] + p[0]) / 2, (start[1] + p[1]) / 2]


for point in start_points:
    draw_point(point)

done = False

random_point = [random.randrange(1, 800), random.randrange(1, 600)]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    draw_point(random_point)
    random_point = new_point(random_point)
    pygame.display.flip()
