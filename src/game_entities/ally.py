import src.globals as gb
from pygame import draw
from src.constants import *
from src.services.trivia import Trivia

class Ally():
    def __init__(self, x:float, y:float, question:str, speed:float=0.02) -> None:
        self.x = x + 0.5
        self.y = y + 0.5
        self.question = question

    def hit(self):
        gb.entity_stack.remove(self)

    def update(self):
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            gb.on_trivia = True
            gb.trivia = Trivia(self, True)

    def draw(self):
        gb.screen.surface.blit(gb.asset['ally'], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 4) * gb.screen.resolution + gb.screen.width/2)))