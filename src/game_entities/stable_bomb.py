from pygame import draw
import src.globals as gb
from src.constants import *

class StableBomb:
    def __init__(self, x:int, y:int) -> None:
        self.x = x + 0.5
        self.y = y + 0.5
    
    def hit(self):
        gb.entity_stack.remove(self)

    def update(self):
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            gb.player.item = "bomb"
            gb.entity_stack.remove(self)
    
    def draw(self):

        gb.screen.surface.blit(gb.asset['bomb'], 
                                ((((self.x - gb.player.x) * 16 - 8) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))