import pygame

class TileKind:
    def __init__(self, name, image, solidity):
        self.name = name
        self.image = pygame.image.load(image)
        self.solidity = solidity
    


class Map:
    def __init__(self, map_file, tile_kind, tile_size):
        self.tile_kinds = tile_kinds

         # load file
        file = open(map_file, "r")
        data = file.read()
        file.close()

         # set up tiles from loaded data
        self.tiles = []
        for line in data.split("\n"):
             row = []
             for tile_number in line:
                 row.append(int(tile_number))
            
        # set size
        self.tile_size = tile_size
    
    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size, y * self.tile_size)
                image = self.tile_kinds[tile].image
                screen.blit(image, location)