import src.globals as gb
from src.utils.resources import *
from src.utils.constants import *
from pygame import Surface, mouse, Rect

class Button:
    def __init__(self, x, y, text:str = "", event:str = "") -> None:
        self.x = x
        self.y = y
        self.asset = assets['button']
        self.width = self.asset.get_width()
        self.height = self.asset.get_height()
        self.text = text
        self.event = event
        self.pressed = False

    def is_hover(self):
        #Verifica se o cursor do mouse está dentro do retangulo do botao
        rect = Rect(self.x, self.y, self.width, self.height)
        return rect.collidepoint(mouse.get_pos())
    
    def draw(self, screen):
        #Altera a cor da letra quando o mouse está em cima
        screen.surface.blit(self.asset, (self.x, self.y))
        button_text = fonts['32'].render(str(self.text).center(20), True, WHITE if self.is_hover() else BLACK)
        screen.surface.blit(button_text, (self.x, self.y+30))  
        #Quando ele soltar o click do mouse, o evento disparará
        if self.is_hover() and mouse.get_pressed()[0]:
            self.pressed = True
        else:
            if self.pressed == True:
                gb.event = self.event
                self.pressed = False
