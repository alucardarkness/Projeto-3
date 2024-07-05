from src.game_entities.bomb import Bomb
from pygame import time
from math import sqrt
import src.globals as gb

class Player:
    def __init__(self, x:float = 1.5, y:float = 1.5, speed:float = 0.05, hp:int = 4, points:int = 0, time:int = 60, name:str = "Player 1") -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.item = "bomb"
        self.hp = hp
        self.points = points
        self.time = time
        self.last_death = (int(self.x), int(self.y))
        self.name = name

    def respawn(self, x:float = 1.5, y:float = 1.5, speed:float = 0.05, hp:int = 4, time:int = 60):
        self.x = x
        self.y = y
        self.speed = speed
        self.item = "bomb"
        self.hp = hp
        self.time = time
        self.vector2 = [0, 0] 
        self.last_death = (int(self.x), int(self.y))

    def update(self):
        if gb.key_dict['Q']: self.use_item()
        if gb.maze.maze[int(self.x)][int(self.y)] == 'S':
            if gb.level < 5:
                gb.event = 'phase_complete'
            else:
                gb.event = 'game_over'
        if self.hp > 5: self.hp = 5
        self.move()
        
    def use_item(self):
        match self.item:
            case "bomb": 
                gb.entity_stack.append(Bomb(self.x, self.y))
                self.item = None
            
    def hit(self):
        self.hp -= 1
        self.last_death = (int(self.x), int(self.y))
        self.x = 1.5
        self.y = 1.5
        if self.hp <= 0:
            gb.event = 'gameover'
        
    def move(self):
        self.vector2 = [0, 0]
        if gb.key_dict['D']: self.vector2[0] += 1
        if gb.key_dict['A']: self.vector2[0] -= 1
        if gb.key_dict['W']: self.vector2[1] -= 1
        if gb.key_dict['S']: self.vector2[1] += 1
            
        match self.vector2:
            case [1,0]: 
                if gb.maze.maze[int(self.x+0.2 + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed * sqrt(2) 
            case [-1,0]: 
                if gb.maze.maze[int(self.x-0.2 - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed * sqrt(2) 
            case [0,1]: 
                if gb.maze.maze[int(self.x)][int(self.y+0.2 + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed * sqrt(2) 
            case [0,-1]: 
                if gb.maze.maze[int(self.x)][int(self.y-0.2 - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed * sqrt(2) 
            case [1,1]: 
                if gb.maze.maze[int(self.x+0.2 + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed 
                if gb.maze.maze[int(self.x)][int(self.y+0.2 + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed
            case [1,-1]: 
                if gb.maze.maze[int(self.x+0.2 + self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x += self.speed
                if gb.maze.maze[int(self.x)][int(self.y-0.2 - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed
            case [-1,1]: 
                if gb.maze.maze[int(self.x-0.2 - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed
                if gb.maze.maze[int(self.x)][int(self.y+0.2 + self.speed * sqrt(2))] != '#': 
                    self.y += self.speed
            case [-1,-1]: 
                if gb.maze.maze[int(self.x-0.2 - self.speed * sqrt(2))][int(self.y)] != '#': 
                    self.x -= self.speed
                if gb.maze.maze[int(self.x)][int(self.y-0.2 - self.speed * sqrt(2))] != '#': 
                    self.y -= self.speed
            


    def draw(self):
        current_sprite = (int(self.speed * time.get_ticks()) % 20) // 5
        match self.vector2:
            case [0, 0]: gb.screen.surface.blit(gb.asset['player_front'][0], (gb.screen.width/2 - 4 * gb.screen.resolution, gb.screen.height/2 - 8 * gb.screen.resolution))
            case [0, 1]: gb.screen.surface.blit(gb.asset['player_front'][current_sprite], (gb.screen.width/2 - 4 * gb.screen.resolution, gb.screen.height/2 - 8 * gb.screen.resolution))
            case [0, -1] | [1, -1] | [-1, -1]: gb.screen.surface.blit(gb.asset['player_back'][current_sprite], (gb.screen.width/2 - 4 * gb.screen.resolution, gb.screen.height/2 - 8 * gb.screen.resolution))
            case [1, 0] | [1, 1]: gb.screen.surface.blit(gb.asset['player_right'][current_sprite], (gb.screen.width/2 - 4 * gb.screen.resolution, gb.screen.height/2 - 8 * gb.screen.resolution))
            case [-1, 0] | [-1, 1]: gb.screen.surface.blit(gb.asset['player_left'][current_sprite], (gb.screen.width/2 - 4 * gb.screen.resolution, gb.screen.height/2 - 8 * gb.screen.resolution))