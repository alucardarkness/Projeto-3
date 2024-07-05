import src.globals as gb
from src.services.maze_path_tracker import PathTracker
from pygame import draw
from src.constants import *
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
        vector2 = [0, 0]
        if round(self.x, 1) != self.next_x: vector2[0] = 1 if self.next_x > self.x else -1
        if round(self.y, 1) != self.next_y: vector2[1] = 1 if self.next_y > self.y else -1
        self.x += vector2[0] * self.speed
        self.y += vector2[1] * self.speed
        
        if abs(gb.player.x - self.x) < 0.5 and abs(gb.player.y - self.y) < 0.5:
            gb.player.hit()

        if (((int(self.x) == int(gb.player.x) and self.y - gb.player.y < 5 and self.y - gb.player.y > 0 and vector2 == [0, -1]) or
            (int(self.x) == int(gb.player.x) and gb.player.y - self.y < 5 and gb.player.y - self.y > 0 and vector2 == [0, 1]) or
            (int(self.y) == int(gb.player.y) and self.x - gb.player.x < 5 and self.x - gb.player.x > 0 and vector2 == [-1, 0]) or
            (int(self.y) == int(gb.player.y) and gb.player.x - self.x < 5 and gb.player.x - self.x > 0 and vector2 == [1, 0]))
            and is_path_free(int(self.x), int(self.y), int(gb.player.x), int(gb.player.y))
            and gb.maze.maze[int(gb.player.x)][int(gb.player.y)] != 'E'):
            self.speed = self.default_speed * 4
            self.path = [(int(gb.player.x), int(gb.player.y))]
        else:
            self.speed = self.default_speed
    def draw(self):
        gb.screen.surface.blit(gb.asset['enemy'], 
                                ((((self.x - gb.player.x) * 16 - 4) * gb.screen.resolution + gb.screen.width/2), 
                                 (((self.y - gb.player.y) * 16 - 4) * gb.screen.resolution + gb.screen.width/2)))