import pygame, sys
from settings import*

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() #initialized!

pygame.display.set_caption('DuckGame')

WINDOW_SIZE = (320,180)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) #initialized window

duckImage = pygame.image.load('DuckGame/duck.png')

moving_right = False
moving_left = False
moving_up = False
moving_down = False

duckLocation = [50, 50]

while True:
    screen.fill((146, 244, 255))

    screen.blit(duckImage, duckLocation)
    if moving_right == True:
        duckLocation[0] += 4
    if moving_left == True:
        duckLocation[0] -= 4
    if moving_up == True:
        duckLocation[1] -= 4
    if moving_down == True:
        duckLocation[1] += 4
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                moving_up = True
            if event.key == K_DOWN:
                moving_down = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_UP:
                moving_up = False
            if event.key == K_DOWN:
                moving_down = False

        
    pygame.display.update()
    clock.tick(60)