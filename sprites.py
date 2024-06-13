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

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

npc_talk_distance = 30

class Villager(pygame.sprite.Sprite):
    def __init__(self, game, villager_name, colour, x, y): 
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        self.villager_name = villager_name
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = 2 * TILESIZE 

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def on(self, distance):
        if distance < npc_talk_distance:
            self.game.state[self.villager_name]["close_enough"] = True
        else:
            self.game.state[self.villager_name]["close_enough"] = False
        
    def update(self):
        from main import global_player
        player = global_player

        # get mouse position   
        pos = pygame.mouse.get_pos()

        d = distance(player.rect.x / 2, 
                            player.rect.y,
                            self.rect.x / 2,
                            self.rect.y)
        
        self.on(d)                
        
        


        # delete self.clicked
        # change else statement