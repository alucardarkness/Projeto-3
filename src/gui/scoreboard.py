import src.globals as gb
from src.gui.back_button import BackButton
from pygame import draw, Rect
from src.constants import *

class Scoreboard:
    def __init__(self) -> None:
        self.back_button = BackButton(180, 115, event='close')

    def draw(self):
        gb.screen.surface.blit(gb.asset['hub'], (0, 0))
        self.back_button.draw()
        for line in gb.scoreboard:
            print(line)