import pygame
from pygame.sprite import Group
from config import *
from timeit import default_timer as timer
import math
import random
from worst_subject import distance

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE 

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

npc_talk_distance = 50

class Villager(pygame.sprite.Sprite):
    def __init__(self, game, x, y): 
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = 2 * TILESIZE 

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.clicked = False

    def on(self, other, distance):
        if distance < npc_talk_distance and self.clicked == True:
            self.game.state["closeEnough"] = True
        else:
            self.game.state["closeEnough"] = False
            self.clicked = False
        

    def update(self):
        from main import global_player
        player = global_player

        # get mouse position   
        pos = pygame.mouse.get_pos()

        d = distance(player.rect.x / 2, 
                            player.rect.y,
                            self.rect.x / 2,
                            self.rect.y)
        
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            print('CLICKED')
            self.clicked = True

        self.on(player, d)
        
        


        # delete self.clicked
        # change else statement