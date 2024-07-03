from src.utils.screen import Screen
from pygame import draw
class Player:
    def __init__(self, x:float = 1.5, y:float = 1.5, speed:float = 1) -> None:
        self.x = x
        self.y = y
        self.speed = speed
    
    def move(self, key_dict:dict):
        if key_dict['D']: self.x += self.speed
        if key_dict['A']: self.x -= self.speed
        if key_dict['W']: self.y -= self.speed
        if key_dict['S']: self.y += self.speed

    def draw(self, screen:Screen):
        draw.circle(screen.surface, 
                    (255, 125, 0), 
                    (screen.width/2, screen.width/2), 
                    (5 * screen.resolution))