from pygame import draw
import src.globals as gb
from src.constants import *

class Clock:
    def __init__(self, x:int, y:int, bonus_time:int=10) -> None:
        self.x = x + 0.5
        self.y = y + 0.5
        self.bonus_time = bonus_time
    
    def update(self):
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            gb.player.time += self.bonus_time
            gb.entity_stack.remove(self)
    
    def draw(self):
        gb.screen.surface.blit(gb.asset['clock'], 
                                ((((self.x - gb.player.x) * 16 - 8) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))