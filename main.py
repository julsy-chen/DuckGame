import pygame
from sprites import *
from config import *
import sys
from pytmx.util_pygame import load_pygame

#tmx_data = load_pygame('/juliachen/DuckGame/Graphics/first-village.tmx')


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

# first village npcs
grandpapa_conversations = parseNpcFile("grandpapa.npc")
baker_conversations = parseNpcFile("baker.npc")

# forest npcs
forest_1_conversations = parseNpcFile("forest_1.npc")
forest_2_conversations = parseNpcFile("forest_2.npc")
forest_3_conversations = parseNpcFile("forest_3.npc")
forest_4_conversations = parseNpcFile("forest_4.npc")
forest_child_conversations = parseNpcFile("forest_child.npc")

# mines npcs
miner_1_conversations = parseNpcFile("miner_1.npc")
miner_2_conversations = parseNpcFile("miner_2.npc")
miner_3_conversations = parseNpcFile("miner_3.npc")
exit_miner_1_conversations = parseNpcFile("exit_miner_1.npc")
map_instructions = parseNpcFile("map.npc")

# ocean
mermaids_conversation = parseNpcFile("mermaids.npc")

# other village
fiance_conversations = parseNpcFile("fiance.npc")



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock() 
        self.running = True
        self.state = {
            "grandpapa" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : grandpapa_conversations}, 
            "baker" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : baker_conversations}, 
            "Jasper" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : forest_1_conversations},  
            "Jake" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : forest_2_conversations},
            "John" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : forest_3_conversations},  
            "Jeff" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : forest_4_conversations},
            "Child" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : forest_child_conversations},  
            "Tremaine" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : miner_1_conversations},  
            "Starved" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : miner_2_conversations},  
            "Kidnapped" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : miner_3_conversations},  
            "TremaineExit" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : exit_miner_1_conversations},
            "Map" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : map_instructions},
            "Mermaids" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : mermaids_conversation},
            "fiance" : {"close_enough" : False, "npc_conversation_index" : 0, "npc_line_index" : 0, "conversations" : fiance_conversations}        
                      }

        self.show_text = False

    def new(self):
        # new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1, 2)
        self.grandpapa = Villager(self, "grandpapa", GREEN, 3, 4)
        self.baker = Villager(self, "baker", GREEN, 13, 4)

        self.forest1 = Villager(self, "Jasper", GREEN, 23, 4)
        self.forest2 = Villager(self, "Jake", GREEN, 33, 4)
        self.forest3 = Villager(self, "John", GREEN, 43, 4)
        self.forest4 = Villager(self, "Jeff", GREEN, 53, 4)
        self.child = Villager(self, "Child", GREEN, 53, 14)

        self.miner1 = Villager(self, "Tremaine", GREEN, 3, 14)
        self.miner2 = Villager(self, "Starved", GREEN, 13, 14)
        self.miner3 = Villager(self, "Kidnapped", GREEN, 23, 14)
        self.map = Villager(self, "Map", YELLOW, 33, 14)
        self.miner1_exit = Villager(self, "TremaineExit", GREEN, 43, 14)        
        
        self.mermaids = Villager(self, "Mermaids", GREEN, 3, 24)

        self.fiance = Villager(self, "fiance", GREEN, 31, 24)

    def events(self):
        # if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        ev = pygame.event.get()
        for event in ev:
             if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

             if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_text == False:
                    for npc, val in self.state.items():
                        if val["close_enough"]:
                            self.show_text = True
                else:
                    for npc, val in self.state.items():
                        if val["close_enough"]:
                            conversations = val["conversations"]
                            conversation_index = val["npc_conversation_index"]
                            current_conversation = conversations[conversation_index]
                            line_index = val["npc_line_index"]

                            if line_index == len(current_conversation) - 1:
                                if val["npc_conversation_index"] != len(conversations) - 1:
                                    val["npc_conversation_index"] += 1
                                val["npc_line_index"] = 0
                                self.show_text = False

                            else:
                                val["npc_line_index"] += 1 

    def update(self):
        # game loops updates
        self.all_sprites.update()

    def draw(self):
        # game loop draw
        self.screen.fill(BLACK)

        for npc, val in self.state.items():
            if val["close_enough"] and self.show_text:
                conversations = val["conversations"]
                conversation_index = val["npc_conversation_index"]
                line_index = val["npc_line_index"]
                current_conversation = conversations[conversation_index]
                current_line = current_conversation[line_index]

                self.draw_text(current_line, font, GREEN, 3, 10)

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

