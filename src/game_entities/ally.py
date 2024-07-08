import src.globals as gb
from src.utils.resources import *
from src.services.trivia import Trivia
from pygame import time
import src.globals as gb
import csv
from src.utils.constants import *

class Ally:
    def __init__(self, x:int, y:int, id:int, question_id:int=0, asset_id='ally') -> None:
        self.x = x
        self.y = y
        self.id = id
        self.question = question_id
        self.asset_id = asset_id
        self.height = assets[asset_id].get_height()
        self.width = assets[asset_id].get_width()

    def effect(self):
        #Entra no modo trivia e cria uma nova trivia para ser respondida
        gb.on_trivia = True
        gb.trivia = Trivia(self, is_ally = True)
        
    
    def hit(self):
        #Remove a estátua do arquivo de aliados quando a trivia dela for respondida (corretamente ou nao)
        if self.id > 0:
            with open(STATUES_FILE) as r, open(STATUES_FILE, 'w', newline='') as w:
                reader = csv.reader(r)
                writer = csv.writer(w)
                for line in reader:
                    if int(line[0]) != self.id:
                        writer.writerow(line)
        #Remove a estatua da pilha de entidades
        gb.entity_stack.remove(self)

    def update(self):
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            self.effect()

    def draw(self, screen):
        screen.surface.blit(assets[self.asset_id], 
                                ((((self.x - gb.player.x) * 16) * screen.resolution - self.width/2 + screen.width/2), 
                                 (((self.y - gb.player.y) * 16) * screen.resolution - self.height/2 + screen.height/2)))