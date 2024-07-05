import src.globals as gb
from src.gui.button import Button
from pygame import draw, Rect
from src.constants import *

class Pause:
    def __init__(self) -> None:
        self.continue_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2 - 100, text='Continue', event='escape')
        self.restart_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2, text=' Restart', event='restart')
        self.exit_button = Button(gb.screen.width/2 - 64*2, gb.screen.height/2 - 21*2 + 100, text='  Exit', event='close')

    def draw(self):
        gb.screen.surface.blit(gb.asset['book'], (gb.screen.width/2 - 146 * 1.5, gb.screen.height/2 - 180 * 1.5))  
        self.continue_button.draw()
        self.restart_button.draw()
        self.exit_button.draw()