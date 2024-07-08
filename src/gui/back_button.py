import src.globals as gb
from src.utils.constants import *
from pygame import Surface, mouse, Rect
from src.utils.resources import assets

class BackButton:
    def __init__(self, x, y, event:str = "") -> None:
        self.x = x
        self.y = y
        self.asset = assets['back_button']
        self.width = self.asset.get_width()
        self.height = self.asset.get_height()
        self.event = event
        self.pressed = False

    def is_hover(self):
        #Verifica se o cursor do mouse está dentro do retangulo do botao
        rect = Rect(self.x, self.y, self.width, self.height)
        return rect.collidepoint(mouse.get_pos())
    
    def draw(self, screen):
        #Se o mouse estiver sobre o botao, ele troca o sprite para hover
        screen.surface.blit(assets['back_button_hover'], (self.x, self.y)) if self.is_hover() else screen.surface.blit(assets['back_button'], (self.x, self.y))
        #Quando ele soltar o click do mouse, o evento disparará
        if self.is_hover() and mouse.get_pressed()[0]:
            self.pressed = True
        else:
            if self.pressed == True:
                gb.event = self.event
                self.pressed = False

