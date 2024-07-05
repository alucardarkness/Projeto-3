import src.globals as gb
from src.gui.button import Button
from pygame import draw, Rect
from src.constants import *

class GameUi:
    def __init__(self) -> None:
        pass
    def draw(self):
        for i in range(gb.player.hp):
            gb.screen.surface.blit(gb.asset['heart'], (40 * i , 10))
        # Level indication
        level_text = gb.font.render(f"level {gb.level}", True, BLACK)
        clock_text = gb.font.render(str(gb.player.time).rjust(10) if gb.player.time > 0 else 'game_over!', True, BLACK)
        score_text = gb.font.render("Score: " + str(gb.player.points).rjust(3), True, BLACK)
        item_text = gb.font16.render(f"Press [Q]", True, BLACK)
        gb.screen.surface.blit(level_text, (gb.screen.width - 100, 10))  
        gb.screen.surface.blit(clock_text, (gb.screen.width/2 - 100, 10))  
        gb.screen.surface.blit(score_text, (10, 50))  
        gb.screen.surface.blit(gb.asset['frame'], (gb.screen.width - 100, 50))
        gb.screen.surface.blit(item_text, (gb.screen.width - 95, 130))  

        if gb.player.item: 
            gb.screen.surface.blit(gb.asset['bomb'], (gb.screen.width - 95, 55))