import src.globals as gb
from src.utils.resources import *
from src.gui.button import Button
from pygame import draw, Rect
from src.utils.constants import *

class Pause:
    def __init__(self, screen) -> None:
        self.continue_button = Button(screen.width/2 - 64*2, screen.height/2 - 21*2 - 100, text='Continue', event='escape')
        self.restart_button = Button(screen.width/2 - 64*2, screen.height/2 - 21*2, text=' Restart', event='restart')
        self.exit_button = Button(screen.width/2 - 64*2, screen.height/2 - 21*2 + 100, text='Save and Exit', event='close')

    def draw(self, screen):
        #Desenha a mini tela com os 3 botões
        screen.surface.blit(assets['book'], (screen.width/2 - 146 * 1.5, screen.height/2 - 180 * 1.5))  
        self.continue_button.draw(screen)
        self.restart_button.draw(screen)
        self.exit_button.draw(screen)