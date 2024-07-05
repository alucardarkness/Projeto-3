import src.globals as gb
from src.gui.back_button import BackButton
from pygame import draw, Rect
from src.constants import *

class About:
    def __init__(self) -> None:
        self.back_button = BackButton(180, 115, event='close')

    def draw(self):
        gb.screen.surface.blit(gb.asset['hub'], (0, 0))
        self.back_button.draw()
        count = 0
        title = gb.font.render('Labirintos da Unicamp', True, BLACK)
        gb.screen.surface.blit(title, (gb.screen.width/2 - 150, gb.screen.height/2 - 230))  
        for line in ABOUT:
            count += 1
            score_text = gb.font16.render(line, True, BLACK)
            gb.screen.surface.blit(score_text, (gb.screen.width/2 - 150, gb.screen.height/2 - 200 + 20 * count))  