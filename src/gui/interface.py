import src.globals as gb
from pygame import draw, Rect
from src.constants import *

class Interface:
    def __init__(self) -> None:
        pass

    def draw(self):
        draw.rect(gb.screen.surface, (255,0,0), Rect(10, 10, 32 * gb.player.hp, 32))    
        # Level indication
        level_text = gb.font.render(f"level {gb.level}", True, BLACK)
        clock_text = gb.font.render(str(gb.timer).rjust(3) if gb.timer > 0 else 'game_over!', True, BLACK)
        gb.screen.surface.blit(level_text, (gb.screen.width - 100, 10))  
        gb.screen.surface.blit(clock_text, (gb.screen.width/2 - 100, 10))  
