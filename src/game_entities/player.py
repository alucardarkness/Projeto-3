from src.utils.screen import Screen
from src.game_entities.bomb import Bomb
from src.services.random_maze_gen import Maze
from pygame import draw
from math import sqrt
import src.globals as gb

class Player:
    def __init__(self, x:float = 1.5, y:float = 1.5, speed:float = 0.02) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.item = "bomb"
    
    def update(self):
        if gb.key_dict['Q']: self.use_item()
        self.move()
        
    def use_item(self):
        match self.item:
            case "bomb": 
                gb.entity_stack.append(Bomb(self.x, self.y))
                self.item = None
            
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
        draw.circle(gb.screen.surface, 
                    (255, 125, 0), 
                    (gb.screen.width/2, gb.screen.width/2), 
                    (5 * gb.screen.resolution))