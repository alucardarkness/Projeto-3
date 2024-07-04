from src.game_entities.bomb import Bomb
from pygame import draw
from math import sqrt
import src.globals as gb

class Player:
    def __init__(self, x:float = 1.5, y:float = 1.5, speed:float = 0.1, hp:int = 4, points:int = 0, time:int = 60) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.item = "bomb"
        self.hp = hp
        self.points = points
        self.time = time
    
    def update(self):
        if gb.key_dict['Q']: self.use_item()
        self.move()
        
    def use_item(self):
        match self.item:
            case "bomb": 
                gb.entity_stack.append(Bomb(self.x, self.y))
                self.item = None
            
    def hit(self):
        self.hp -= 1
        self.x = 1.5
        self.y = 1.5
        
    def move(self):
        vector2 = [0, 0]
        if gb.key_dict['D']: vector2[0] += 1
        if gb.key_dict['A']: vector2[0] -= 1
        if gb.key_dict['W']: vector2[1] -= 1
        if gb.key_dict['S']: vector2[1] += 1
            
        match vector2:
            case [1,0]: 
                if gb.maze.maze[int(self.x + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed * sqrt(2) 
            case [-1,0]: 
                if gb.maze.maze[int(self.x - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed * sqrt(2) 
            case [0,1]: 
                if gb.maze.maze[int(self.x)][int(self.y + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed * sqrt(2) 
            case [0,-1]: 
                if gb.maze.maze[int(self.x)][int(self.y - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed * sqrt(2) 
            case [1,1]: 
                if gb.maze.maze[int(self.x + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed 
                if gb.maze.maze[int(self.x)][int(self.y + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed
            case [1,-1]: 
                if gb.maze.maze[int(self.x + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed
                if gb.maze.maze[int(self.x)][int(self.y - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed
            case [-1,1]: 
                if gb.maze.maze[int(self.x - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed
                if gb.maze.maze[int(self.x)][int(self.y + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed
            case [-1,-1]: 
                if gb.maze.maze[int(self.x - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed
                if gb.maze.maze[int(self.x)][int(self.y - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed
            


    def draw(self):
        gb.screen.surface.blit(gb.asset['player'], (gb.screen.width/2 - 4 * gb.screen.resolution, gb.screen.width/2 - 4 * gb.screen.resolution))