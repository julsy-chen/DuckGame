import pygame

class TileKind:
    def __init__(self, name, image, solidity):
        self.name = name
        self.image = pygame.image.load(image)
        self.solidity = solidity 