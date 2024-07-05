import src.globals as gb
from src.utils.constants import *
import pygame
class TriviaButton:
    def __init__(self, x, y, width:int = 64*3, height:int = 21*3, num:int = 0) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num = num
        self.pressed = False

    def is_hover(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.x and mouse_x < self.x + self.width and mouse_y > self.y and mouse_y < self.y + self.height:
            return True
        return False
    def draw(self):
        gb.screen.surface.blit(gb.asset['trivia_button'], (self.x, self.y))
        button_text = gb.font16.render(str(gb.trivia.answers[self.num-1]), True, WHITE if self.is_hover() else BLACK)
        gb.screen.surface.blit(button_text, (self.x + 20, self.y+25))  
        if self.is_hover() and pygame.mouse.get_pressed()[0]:
            self.pressed = True
        else:
            if self.pressed == True:
                gb.trivia.submit(self.num)
                self.pressed = False
