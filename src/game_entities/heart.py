from pygame import time
import src.globals as gb
from src.utils.constants import *

class Heart:
    def __init__(self, x:int, y:int) -> None:
        self.x = x + 0.5
        self.y = y + 0.5
    
    def hit(self):
        gb.entity_stack.remove(self)

    def update(self):
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            if gb.player.hp < 5: gb.player.hp += 1 
            gb.entity_stack.remove(self)
    
    def draw(self):
        current_sprite = (time.get_ticks() % 1500) // 750
        gb.screen.surface.blit(gb.asset['heart'], 
                                ((((self.x - gb.player.x) * 16 - 4.5) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 5.5 + 2 * current_sprite) * gb.screen.resolution + gb.screen.width/2)))