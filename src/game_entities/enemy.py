import src.globals as gb
from src.services.maze_path_tracker import PathTracker
from pygame import draw
from src.constants import *
class Enemy():
    def __init__(self, x:float, y:float, question:str, speed:float=0.05) -> None:
        self.x = x
        self.y = y
        self.question = question
        self.speed = speed
        self.path = PathTracker(int(self.x), int(self.y)).path
        self.next_x = self.x
        self.next_y = self.y
        
    def update(self):
        if len(self.path) == 0:
            self.path = PathTracker(int(self.x), int(self.y)).path
        if self.next_x == round(self.x, 1) and self.next_y == round(self.y, 1):
            x, y = self.path.pop(0)
            self.next_x = x+0.5
            self.next_y = y+0.5
        vector2 = [0, 0]
        if round(self.x, 1) != self.next_x: vector2[0] = 1 if self.next_x > self.x else -1
        if round(self.y, 1) != self.next_y: vector2[1] = 1 if self.next_y > self.y else -1
        self.x += vector2[0] * self.speed
        self.y += vector2[1] * self.speed
        
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            gb.player.hit()
    def draw(self):
        gb.screen.surface.blit(gb.asset['enemy'], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 4) * gb.screen.resolution + gb.screen.width/2)))