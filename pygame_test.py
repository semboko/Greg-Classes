import pygame
from random import randint


pygame.init()
basic_surface = pygame.display.set_mode((500, 500))

x = 250
y = 250

color = (255, 0, 0)

while True:
    # 1. Processing events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color = (r, g, b)

    # 2. Drawing a new frame
    basic_surface.fill((255, 255, 255))
    pygame.draw.circle(basic_surface, color, (x, y), 100)

    # 3. Removing the last frame and showing the new one
    pygame.display.update()
