import pygame
from sprites import *
from config import *
import sys
from pytmx.util_pygame import load_pygame

#tmx_data = load_pygame('/juliachen/DuckGame/Graphics/first-village.tmx')

# dialogue
line1 = "Hello my child, go deliver these five fish to the people in the village and bring the extra fish back to me"

#fileName -> [[hello, goodbye], [blahblahblah]]
#
#fileName:
# hello
# goodbye
# done
# blahblahblah
# done
#
# read the file
# parse the string
# return the "conversations"
def parseNpcFile(fileName):
    f = open(fileName, "r")
    raw_file_text = f.read()
    split_text = raw_file_text.splitlines() 
    npc_conversations = []
    temp = []
    for text in split_text:
        if text != "DONE":
            temp.append(text)
        else:
            npc_conversations.append(temp)
            temp = []
    
    return npc_conversations

# storing npc conversations 
grandpapa_conversations = parseNpcFile("grandpapa.npc")

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock() 
        self.running = True
        self.state = {"closeEnough" : False}

    def new(self):
        # new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1, 2)
        self.grandpapa = Villager(self, 3, 4)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loops updates
        self.all_sprites.update()

    def draw(self):
        # game loop draw
        self.screen.fill(BLACK)
        if self.state["closeEnough"] == True:
            self.draw_text(line1, font, GREEN, 10, 200)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))


    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
        self.running = False

    def intro_screen(self):
        pass

    


g = Game()
g.intro_screen()
g.new()
global_player = g.player
while g.running:
    g.main()
pygame.quit()
sys.exit

