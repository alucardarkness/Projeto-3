import src.globals as gb
from src.utils.constants import *
from src.utils.resources import *

from pygame import Surface, mouse, Rect
class TriviaButton:
    def __init__(self, x, y, num:int = 0) -> None:
        self.x = x
        self.y = y
        self.asset = assets['trivia_button']
        self.width = self.asset.get_width()
        self.height = self.asset.get_height()
        self.num = num
        self.pressed = False

    def is_hover(self):
        #Verifica se o mouse esta em cima do botao
        rect = Rect(self.x, self.y, self.width, self.height)
        return rect.collidepoint(mouse.get_pos())
    
    def draw(self, screen):
        #Altera a cor da letra quando o mouse está em cima
        screen.surface.blit(self.asset, (self.x, self.y))
        button_text = fonts['16'].render(str(gb.trivia.answers[self.num-1]), True, WHITE if self.is_hover() else BLACK)
        screen.surface.blit(button_text, (self.x + 20, self.y+25))  
        #Dispara o evento quando solta o click do mouse
        if self.is_hover() and mouse.get_pressed()[0]:
            self.pressed = True
        else:
            if self.pressed == True:
                gb.trivia.submit(self.num)
                self.pressed = False
