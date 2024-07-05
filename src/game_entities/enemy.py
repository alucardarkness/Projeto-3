import src.globals as gb
from src.services.maze_path_tracker import PathTracker
from pygame import time
from src.utils.constants import *
from src.services.trivia import Trivia

class Enemy():
    def __init__(self, x:float, y:float, question:str, speed:float=0.02) -> None:
        self.x = x
        self.y = y
        self.question = question
        self.default_speed = speed
        self.speed = speed
        self.path = PathTracker(int(self.x), int(self.y)).path
        self.next_x = self.x
        self.next_y = self.y
        self.vector2 = [0, 0]

    def hit(self):
        gb.entity_stack.remove(self)

    def update(self):
        def is_path_free(x, y, player_x, player_y):
            for i in range(min(x, player_x), max(x, player_x)+1):
                for j in range(min(y, player_y), max(y, player_y)+1):
                    if gb.maze.maze[i][j] == '#':
                        return False
            return True
        
        if len(self.path) == 0:
            self.path = PathTracker(int(self.x), int(self.y)).path
        if self.next_x == round(self.x, 1) and self.next_y == round(self.y, 1):
            x, y = self.path.pop(0)
            self.next_x = x+0.5
            self.next_y = y+0.5
        self.vector2 = [0, 0]
        if round(self.x, 1) != self.next_x: self.vector2[0] = 1 if self.next_x > self.x else -1
        if round(self.y, 1) != self.next_y: self.vector2[1] = 1 if self.next_y > self.y else -1
        self.x += self.vector2[0] * self.speed
        self.y += self.vector2[1] * self.speed
        
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            gb.on_trivia = True
            gb.trivia = Trivia(self)

        if (((int(self.x) == int(gb.player.x) and self.y - gb.player.y < 5 and self.y - gb.player.y > 0 and self.vector2 == [0, -1]) or
            (int(self.x) == int(gb.player.x) and gb.player.y - self.y < 5 and gb.player.y - self.y > 0 and self.vector2 == [0, 1]) or
            (int(self.y) == int(gb.player.y) and self.x - gb.player.x < 5 and self.x - gb.player.x > 0 and self.vector2 == [-1, 0]) or
            (int(self.y) == int(gb.player.y) and gb.player.x - self.x < 5 and gb.player.x - self.x > 0 and self.vector2 == [1, 0]))
            and is_path_free(int(self.x), int(self.y), int(gb.player.x), int(gb.player.y))
            and gb.maze.maze[int(gb.player.x)][int(gb.player.y)] != 'E'):
            self.speed = self.default_speed * 4
            self.path = [(int(gb.player.x), int(gb.player.y))]
        else:
            self.speed = self.default_speed
    def draw(self):
        current_sprite = (int(self.speed * time.get_ticks()) % 20) // 5
        match self.vector2:
            case [0, 0]: gb.screen.surface.blit(gb.asset['enemy_front'][0], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))
            case [0, 1]: gb.screen.surface.blit(gb.asset['enemy_front'][current_sprite], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))
            case [0, -1] | [1, -1] | [-1, -1]: gb.screen.surface.blit(gb.asset['enemy_back'][current_sprite], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))
            case [1, 0] | [1, 1]: gb.screen.surface.blit(gb.asset['enemy_right'][current_sprite], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))
            case [-1, 0] | [-1, 1]: gb.screen.surface.blit(gb.asset['enemy_left'][current_sprite], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 8) * gb.screen.resolution + gb.screen.width/2)))