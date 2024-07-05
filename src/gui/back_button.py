import src.globals as gb
from src.utils.constants import *
import pygame
class BackButton:
    def __init__(self, x, y, width:int = 23 * 3, height:int = 19 * 3, text:str = "Button", event:str = "") -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.event = event
        self.pressed = False

    def is_hover(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.x and mouse_x < self.x + self.width and mouse_y > self.y and mouse_y < self.y + self.height:
            return True
        return False
    def draw(self):
        gb.screen.surface.blit(gb.asset['back_button_hover'], (self.x, self.y)) if self.is_hover() else gb.screen.surface.blit(gb.asset['back_button'], (self.x, self.y))
        if self.is_hover() and pygame.mouse.get_pressed()[0]:
            self.pressed = True
        else:
            if self.pressed == True:
                gb.event = self.event
                self.pressed = False

