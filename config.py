import pygame

pygame.init()

WIN_WIDTH = 640 
WIN_HEIGHT = 480
TILESIZE = 16
FPS = 60

dialogue_box_width = 400
dialogue_box_height = 200
dialogue_box_x = (WIN_WIDTH - dialogue_box_width) // 2
dialogue_box_y = (WIN_HEIGHT - dialogue_box_height) // 2
dialogue_box = False

PLAYER_LAYER = 1
PLAYER_SPEED = 3

RED = (255, 192, 203)
BLACK = (0, 0, 0)
GREEN = (0, 244, 0)
YELLOW = (255, 252, 211)

font = pygame.font.SysFont("menlo", 10)
