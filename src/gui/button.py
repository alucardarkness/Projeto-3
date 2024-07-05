import src.globals as gb
from src.constants import *
import pygame
class Button:
    def __init__(self, x, y, width:int = 64*4, height:int = 21*4, text:str = "Button", event:str = "") -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.event = event
        self.pressed = False

    def is_hover(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.x and mouse_x < self.x + self.width and mouse_y > self.y and mouse_y < self.y + self.height:
            return True
        return False
    def draw(self):
        gb.screen.surface.blit(gb.asset['button'], (self.x, self.y))
        button_text = gb.font.render(str(self.text).center(20), True, WHITE if self.is_hover() else BLACK)
        gb.screen.surface.blit(button_text, (self.x, self.y+30))  
        if self.is_hover() and pygame.mouse.get_pressed()[0]:
            self.pressed = True
        else:
            if self.pressed == True:
                print(f"event: {self.event}")
                gb.event = self.event
                self.pressed = False
